################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
import shutil
import sys
import platform
import os
import time
from datetime import date
import pandas as pd
from os import listdir
from os.path import isfile, join
import ntpath
import imaplib as plt
from skimage.filters import threshold_multiotsu
# from sklearn.tests.test_base import K
from tensorflow.python.keras.models import load_model
from tqdm import tqdm
from mahotas import gaussian_filter
import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np
from scipy.io import savemat
import tempfile
from PyQt5.QtCore import pyqtSignal
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
#                             QSize, QTime, QUrl, Qt, QEvent, QThread)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
#                            QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
# from PySide2.QtWidgets import *
from PIL.ImageQt import ImageQt
from PIL import Image
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDesktopWidget, QFrame, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QPixmap)
from skimage.filters import threshold_multiotsu
from tensorflow.python.keras.models import load_model
from sklearn.model_selection import train_test_split
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
import multiprocessing as mp
# GUI FILE
from ui_main import Ui_MainWindow, QPixmap
from ui_show_images import Ui_Segmented_images
# IMPORT FUNCTIONS
from ui_functions import *

# Global paramenters
# images/masks dic: key = image/mask file name
#                   value = image/mask file path
models_dic = {}
images_segmentation_dic = {}
segmented_images_dic = {}  # segmented images dic: key = segmented image file name
#                   value = segmented image numpy array
images_train_dic = {}
masks_train_dic = {}

num_segmentation_selected_images = 0
num_segmentation_unselected_images = 0

num_train_selected_images = 0
num_train_unselected_images = 0
num_train_selected_masks = 0
num_train_unselected_masks = 0

BATCH_WIDTH = 512
BATCH_HIGHT = 512

stop_training_flag = False
training = True


# Help functions

def update_batch_size(image_size):
    global BATCH_WIDTH
    global BATCH_HIGHT
    if image_size != BATCH_WIDTH:
        BATCH_WIDTH = image_size
        BATCH_HIGHT = image_size


def set_stylesheet_listitem(item):
    font = QtGui.QFont('Arial', 10)
    font.setBold(True)
    font.setWeight(75)
    item.setFont(font)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.NoBrush)
    item.setForeground(brush)


def contrastStretching(im):
    b = im.max()
    a = im.min()
    print(a, b)
    # Converting im1 to float.
    c = im.astype(float)
    # Contrast stretching transformation.
    im1 = 255.0 * (c - a) / (b - a + 0.0000001)
    return im1


def jaccard_similarity(image1: np.ndarray, image2: np.ndarray) -> float:
    """
        Computes the Jaccard similarity , a measure of set similarity.

        Parameters
        ----------
        image1: array-like, bool
            Any array of arbitrary size. If not boolean, will be converted.
        image2: array-like, bool
            Any other array of identical size. If not boolean, will be converted.
        Returns
        -------
        j_s : float
            Jaccard similarity as a float on range [0,1].
            Maximum similarity = 1,
            No similarity = 0

        Notes
        -----
        The order of inputs for `similarity` is irrelevant. The result will be
        identical if `image1` and `image2` are switched.
    """
    im1 = np.asarray(image1).astype(np.bool)
    im2 = np.asarray(image2).astype(np.bool)

    print("true", im1.shape)
    print("pred", im2.shape)
    if im1.shape != im2.shape:
        raise ValueError(
            "Shape mismatch: im1 and im2 must have the same shape.")

    intersection = np.logical_and(im1, im2)
    union = np.logical_or(im1, im2)
    return intersection.sum() / union.sum()


def preprocessImage():
    global images_train_dic
    global masks_train_dic

    print("Starting Preprocessing Images")
    listOfImages = []
    for key in images_train_dic:
        listOfImages.append(images_train_dic[key])
    listOfImages.sort()
    imgInPatches = crop2(listOfImages, BATCH_HIGHT, BATCH_WIDTH)
    del listOfImages
    print("Finished Preprocessing images")
    print("Starting Preprocessing Mask")
    listOfMasks = []
    for key in masks_train_dic:
        listOfMasks.append(masks_train_dic[key])
    listOfMasks.sort()
    mskInPatches = crop2(listOfMasks, BATCH_HIGHT, BATCH_WIDTH)
    del listOfMasks
    print("Finished Preprocessing Mask")
    return imgInPatches, mskInPatches


def crop2(images_path, height, width):
    """
    this function split the original to mutiple patches with sahpe (height,width)
    :param images_path: the path of original image
    :param height: height of patch
    :param width:  width of patch
    :return: list of patches of original image.
    """

    images = []
    for imgpath in tqdm(images_path):

        img = cv2.imread(imgpath, 0) / 255
        imgwidth, imgheight = img.shape
        if imgwidth % width != 0 and imgheight % height != 0:
            img = cv2.resize(img, (imgheight - (imgheight % height), imgwidth - (imgwidth % width)))
        elif imgheight % height != 0:
            img = cv2.resize(img, (imgheight - (imgheight % height), imgwidth))
        elif imgwidth % width != 0:
            img = cv2.resize(img, (imgheight, imgwidth - (imgwidth % width)))

        for i in range(0, imgheight - BATCH_HIGHT, height):
            for j in range(0, imgwidth - BATCH_WIDTH, width):
                patch = img[j:j + width, i:i + height]
                if len(patch.shape) == 3:
                    patch = patch[:, :, :3]
                patch = np.expand_dims(patch, axis=-1)

                images.append(patch)

    return np.asarray(images)


def uNet():
    """
    Function that build the model and compile the model,
     in the end it plot the summery of the model
    :return: The compiled model
    """
    print("---------------------------Building Model--------------------------------")
    inputs = tf.keras.layers.Input((BATCH_HIGHT, BATCH_WIDTH, 1))

    # Contraction path
    c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(inputs)
    c1 = tf.keras.layers.Dropout(0.1)(c1)
    c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c1)
    p1 = tf.keras.layers.MaxPooling2D((2, 2))(c1)

    c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p1)
    c2 = tf.keras.layers.Dropout(0.1)(c2)
    c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c2)
    p2 = tf.keras.layers.MaxPooling2D((2, 2))(c2)

    c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p2)
    c3 = tf.keras.layers.Dropout(0.2)(c3)
    c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c3)
    p3 = tf.keras.layers.MaxPooling2D((2, 2))(c3)

    c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p3)
    c4 = tf.keras.layers.Dropout(0.2)(c4)
    c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c4)
    p4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(c4)

    c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p4)
    c5 = tf.keras.layers.Dropout(0.3)(c5)
    c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c5)

    # Expansive path
    u6 = tf.keras.layers.Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c5)
    u6 = tf.keras.layers.concatenate([u6, c4])
    c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
    c6 = tf.keras.layers.Dropout(0.2)(c6)
    c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)

    u7 = tf.keras.layers.Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c6)
    u7 = tf.keras.layers.concatenate([u7, c3])
    c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
    c7 = tf.keras.layers.Dropout(0.2)(c7)
    c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)

    u8 = tf.keras.layers.Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c7)
    u8 = tf.keras.layers.concatenate([u8, c2])
    c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
    c8 = tf.keras.layers.Dropout(0.1)(c8)
    c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)

    u9 = tf.keras.layers.Conv2DTranspose(16, (2, 2), strides=(2, 2), padding='same')(c8)
    u9 = tf.keras.layers.concatenate([u9, c1], axis=3)
    c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
    c9 = tf.keras.layers.Dropout(0.1)(c9)
    c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)

    outputs = tf.keras.layers.Conv2D(1, (1, 1), activation='sigmoid')(c9)

    model = tf.keras.Model(inputs=[inputs], outputs=[outputs])
    model.compile(optimizer=Adam(lr=1e-4), loss='binary_crossentropy', metrics=['accuracy'])
    model.summary()
    return model


# # ------------------------------------------------------
#

def otsu_threholding(image):
    thresholds = threshold_multiotsu(image, classes=5)

    # Digitize (segment) original image into multiple classes.
    # np.digitize assign values 0, 1, 2, 3, ... to pixels in each class.
    regions = np.digitize(image, bins=thresholds)
    return regions


class MainWindow(QMainWindow):
    def __init__(self):
        # Parameters

        '''
        temp file init
        temp_file_dir = 
        '''
        # current_page = ''

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_temp()

        # Disable buttons that could not be used in the init
        self.disable_all_segmentation_btns()

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        '''-----------------------------------------PAGE 1 Segmentation----------------------------------------------'''
        # PAGE 1 Segmentation
        self.ui.segmentation_page_btn.clicked.connect(self.segmentation_menu_btn)

        # segmentation list updates
        self.ui.segmentation_image_lstwdg.itemChanged.connect(self.update_lcds)
        self.ui.segmentation_image_lstwdg.itemClicked.connect(self.show_image)

        # selecting and deleting images from segmentation list
        self.ui.segmentation_selectall_btn.clicked.connect(self.selectall_images_lstwdg)
        self.ui.segmentation_unselectall_btn.clicked.connect(self.unselectall_images_lstwdg)
        self.ui.segmentation_clear_unselect_images_btn.clicked.connect(self.clear_unselected_images_lstwdg)
        self.ui.segmentation_clearimages_btn.clicked.connect(self.clear_images_lstwdg)

        # Model QComboBox
        self.setUp_QComboBox()
        self.ui.segmentation_batchsize_256_radbtn.toggled.connect(self.update_model_combox)
        self.ui.segmentation_batchsize_512_radbtn.toggled.connect(self.update_model_combox)

        # Raw image QCheckBox
        self.ui.segmentation_rawimg_chbox.stateChanged.connect(self.update_raw)

        # Start Segmentation
        self.ui.segmentation_start_segmentation_btn.clicked.connect(self.start_segmentation)

        # Stop Segmentation
        self.ui.segmentation_stop_segmentation_btn.clicked.connect(self.stop_segmentation)

        # Show Results
        self.ui.segmentation_show_results_btn.clicked.connect(self.show_results)

        # Download Results
        self.ui.segmentation_downloadresults_btn.clicked.connect(self.download_results)

        # Reset
        self.ui.segmentation_reset_btn.clicked.connect(self.reset_page)

        '''------------------------------------------PAGE 2 Training-------------------------------------------------'''
        # PAGE 2 Training
        self.ui.training_page_btn.clicked.connect(self.train_menu_btn)
        self.disable_all_train_btns()

        # Training list updates
        self.ui.train_image_lstwdg.itemChanged.connect(self.update_train_img_lcds)
        self.ui.train_mask_lstwdg.itemChanged.connect(self.update_train_msk_lcds)

        # Training Insert Images
        self.ui.train_browse_image_btn.clicked.connect(self.insert_train_images)

        # Training Insert Masks
        self.ui.train_browse_masks_btn.clicked.connect(self.insert_train_masks)

        # Selecting and deleting images from training list
        self.ui.train_image_selectall_btn.clicked.connect(self.train_selectall_images_lstwdg)
        self.ui.train_image_unselectall_btn.clicked.connect(self.train_unselectall_images_lstwdg)
        self.ui.train_clear_unselect_images_btn.clicked.connect(self.train_clear_unselected_images_lstwdg)
        self.ui.train_clearimages_btn.clicked.connect(self.train_clearimages_lstwdg)

        # Selecting and deleting masks from training list
        self.ui.train_selectall_masks_btn.clicked.connect(self.train_selectall_masks_lstwdg)
        self.ui.train_unselectall_masks_btn.clicked.connect(self.train_unselectall_masks_lstwdg)
        self.ui.train_clear_unselect_masks_btn.clicked.connect(self.train_clear_unselected_masks_lstwdg)
        self.ui.train_cleamasks_btn.clicked.connect(self.train_clearmasks_lstwdg)

        # Start Training
        self.ui.train_start_training_btn.clicked.connect(self.start_training)

        # Stop Training
        self.ui.train_stop_training_btn.clicked.connect(self.stop_training)

        '''------------------------------------------PAGE 3 Help-------------------------------------------------'''
        # PAGE 3 Help
        self.ui.help_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.help_page))

        # PAGE 4 About
        self.ui.about_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about_page))
        self.ui.segmentation_browse_btn.clicked.connect(self.insert_images)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    # Toggle segmentation and train buttons
    def segmentation_menu_btn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.segmentation_page)

    def train_menu_btn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.tarin_page)

    '''-----------------------------------------PAGE 1 Segmentation Functions----------------------------------------'''

    # Buttons functions
    # Insert Images
    def insert_images(self):
        """
        This function is connected with "insert images" button.
        This function upload the images into the images_dic, with key = file name, value = file path.
        And it enbales some buttons that can be used after inserting images.
        In the end it adds the image into the QListWidget and also updates the LCD.
        :return:
        """
        global images_segmentation_dic
        file_to_open = "Image Files (*.png *.jpg *.tif)"
        res = QFileDialog.getOpenFileNames(None, "Open File", "/", file_to_open)
        if len(res[0]) > 0:
            # Disable and enable some button
            self.enable_all_segmentation_btns()
            self.ui.segmentation_downloadresults_btn.setEnabled(False)
            self.ui.segmentation_stop_segmentation_btn.setEnabled(False)
            self.ui.segmentation_show_results_btn.setEnabled(False)

            for img in res[0]:
                if img.split('/')[-1] not in images_segmentation_dic:
                    # insert into dic
                    images_segmentation_dic[img.split('/')[-1]] = img
                    # create list item
                    list_item = QtWidgets.QListWidgetItem()
                    list_item.setCheckState(QtCore.Qt.Checked)
                    list_item.setText(img.split('/')[-1])
                    set_stylesheet_listitem(list_item)
                    # update the lcd
                    self.ui.segmentation_image_lstwdg.addItem(list_item)
                    self.update_lcds(1)
            pixmap = QPixmap(res[0][0])
            pixmap = pixmap.scaled(512, 512, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.ui.segmentation_image_lbl.setPixmap(pixmap)

    # Select/delete images buttons
    def selectall_images_lstwdg(self):
        """
        This function is connected to "select all" button.
        This function change the state of every item in the QListWidget to checked.
        :return:
        """
        for i in range(self.ui.segmentation_image_lstwdg.count()):
            if self.ui.segmentation_image_lstwdg.item(i).checkState() == QtCore.Qt.Unchecked:
                self.ui.segmentation_image_lstwdg.item(i).setCheckState(QtCore.Qt.Checked)

    def unselectall_images_lstwdg(self):
        """
        This function is connected to "unselect all" button.
        This function change the state of every item in the QListWidget to unchecked.
        :return:
        """
        for i in range(self.ui.segmentation_image_lstwdg.count()):
            if self.ui.segmentation_image_lstwdg.item(i).checkState() == QtCore.Qt.Checked:
                self.ui.segmentation_image_lstwdg.item(i).setCheckState(QtCore.Qt.Unchecked)

    def clear_unselected_images_lstwdg(self):
        """
        This function is connected to "clear unselected images" button.
        This function deletes every item in the QListWidget that it's state is unchecked and also updates
        the LCD and the items in the images_segmentation_dic dic.
        :return:
        """
        global images_segmentation_dic
        delete_lst = []
        for i in range(self.ui.segmentation_image_lstwdg.count()):
            if self.ui.segmentation_image_lstwdg.item(i).checkState() == QtCore.Qt.Unchecked:
                delete_lst.append(self.ui.segmentation_image_lstwdg.item(i))
        for item in delete_lst:
            self.ui.segmentation_image_lstwdg.takeItem(self.ui.segmentation_image_lstwdg.row(item))
            images_segmentation_dic.pop(item.text())
            self.update_lcds(-1)

    def clear_images_lstwdg(self):
        """
        This function is connected to the "clear images" button
        This function deletes every item in the QListWidget, updates the LCD and also images_segmentation_dic.
        :return:
        """
        global images_segmentation_dic
        self.ui.segmentation_image_lstwdg.clear()
        del images_segmentation_dic
        images_segmentation_dic = {}
        self.update_lcds(0)

    # Raw image QCheckBox
    def update_raw(self):
        """
        This function reacts when the Raw image QCheckBox state changed.
        It disables show results button
        :return:
        """
        if self.ui.segmentation_rawimg_chbox.checkState():
            self.ui.segmentation_show_results_btn.setEnabled(False)

    # QComboBox
    def setUp_QComboBox(self):
        global models_dic
        onlyfiles = [f for f in listdir("Models/512") if isfile(join("Models/512", f))]
        for f in onlyfiles:
            models_dic[f] = "Model/512/" + f
            self.ui.models_QComboBox.addItem(f)

    def update_model_combox(self):
        """
        This function is connected with the image batch size QRadioBox.
        It changes the QComboBox of models to models that compatible with the image size.
        :return:
        """
        global models_dic
        if self.ui.segmentation_batchsize_512_radbtn.isChecked():
            self.ui.models_QComboBox.clear()
            onlyfiles = [f for f in listdir("Models/512") if isfile(join("Models/512", f))]
            for f in onlyfiles:
                models_dic[f] = "Models/512/" + f
                self.ui.models_QComboBox.addItem(f)
        else:
            self.ui.models_QComboBox.clear()
            onlyfiles = [f for f in listdir("Models/256") if isfile(join("Models/256", f))]
            for f in onlyfiles:
                models_dic[f] = "Models/256/" + f
                self.ui.models_QComboBox.addItem(f)

    # Start Segmentation
    def start_segmentation(self):
        global BATCH_WIDTH
        global BATCH_HIGHT

        if self.ui.segmentation_batchsize_256_radbtn.isChecked():
            BATCH_HIGHT = 256
            BATCH_WIDTH = 256
            model_name = "256/" + self.ui.models_QComboBox.currentText()

        else:
            model_name = "512/" + self.ui.models_QComboBox.currentText()

        self.update_progbar_lbl("Loading Model Named: " + model_name)
        self.update_progbar_lbl(model_name + " Model Loaded Successfully!")
        self.ui.segmentation_reset_btn.setEnabled(False)

        # with tempfile.TemporaryDirectory(dir=os.getcwd()) as tmpdirname:
        msg = ""
        if self.ui.segmentation_rawimg_chbox.checkState():
            msg = "segmentation_raw"
        else:
            msg = "segmentation"
        self.worker = WorkerThread(model_name, msg=msg, parent=None)
        self.worker.start()
        self.ui.segmentation_stop_segmentation_btn.setEnabled(True)
        self.worker.update_progress.connect(self.evt_update_progress)
        self.worker.worker_complete.connect(self.evt_worker_finished)
        self.worker.progbar_lbl_update.connect(self.evt_update_progbar_lbl)

    # Stop Segmentation
    def stop_segmentation(self):
        """
        This function is connected with "Stop Segmentation" button. And it terminates the segmentation thread therefore
        stopping the segmntatio process.
        :return:
        """
        self.worker.terminate()
        self.update_progbar_lbl("")
        self.evt_update_progress(0)
        self.ui.segmentation_stop_segmentation_btn.setEnabled(False)
        self.ui.segmentation_reset_btn.setEnabled(True)

    # Show Results
    def show_results(self):
        self.show_images_popup = Segmented_images()
        self.show_images_popup.show()

    def download_results(self):
        """
        This function downloads the segmented images.
        :return:
        """
        global segmented_images_dic
        if segmented_images_dic:
            filename = QFileDialog.getSaveFileName(self, "Save file", os.getcwd(), ".*")[0]
            path_save, _ = ntpath.split(filename)
            for seg in segmented_images_dic:
                if self.ui.segmentation_rawimg_chbox.checkState():
                    savemat(path_save + '/segmented_raw_' + seg + '.mat', {'mydata': segmented_images_dic[seg]})
                else:
                    cv2.imwrite(path_save + '/segmented_' + seg, segmented_images_dic[seg])

    def reset_page(self):
        global images_segmentation_dic
        global segmented_images_dic
        global num_segmentation_selected_images
        global num_segmentation_unselected_images
        del images_segmentation_dic
        del segmented_images_dic

        images_segmentation_dic = {}
        segmented_images_dic = {}

        self.disable_all_segmentation_btns()
        num_segmentation_selected_images = 0
        num_segmentation_unselected_images = 0
        self.ui.segmentation_image_lstwdg.clear()
        self.ui.segmentation_image_lbl.setText("Please insert image to view on the screen")
        self.update_progbar_lbl("")
        self.evt_update_progress(0)
        self.ui.segmentaion_selected_lcd.display(0)
        self.ui.segmentation_unselected_lcd.display(0)
        self.ui.segmentation_rawimg_chbox.setCheckState(False)

    '''-----------------------------------------PAGE 2 Train---------------------------------------------------------'''

    # Insert Images
    def insert_train_images(self):
        """
                This function is connected with "insert images" button.
                This function upload the images into the images_train_dic, with key = file name, value = path.
                And it enbales some buttons that can be used after inserting images.
                In the end it adds the image into the QListWidget and also updates the LCD.
                :return:
                """
        global images_train_dic
        file_to_open = "Image Files (*.png *.jpg *.tif)"
        res = QFileDialog.getOpenFileNames(None, "Open File", "/", file_to_open)
        if len(res[0]) > 0:
            # Disable and enable some button
            self.enable_train_img_btns()
            for img in res[0]:
                if img.split('/')[-1] not in images_train_dic:
                    # insert into dic
                    images_train_dic[img.split('/')[-1]] = img
                    # create list item
                    list_item = QtWidgets.QListWidgetItem()
                    list_item.setCheckState(QtCore.Qt.Checked)
                    list_item.setText(img.split('/')[-1])
                    set_stylesheet_listitem(list_item)
                    self.ui.train_image_lstwdg.addItem(list_item)
                    # update the lcd
                    self.update_train_img_lcds(1)
        if masks_train_dic and images_train_dic:
            self.ui.train_start_training_btn.setEnabled(True)
        else:
            self.ui.train_start_training_btn.setEnabled(False)

    # Insert Masks
    def insert_train_masks(self):
        """
                This function is connected with "insert Masks" button.
                This function upload the masks into the masks_train_dic, with key = file name, value = path.
                And it enbales some buttons that can be used after inserting masks.
                In the end it adds the masks into the QListWidget and also updates the LCD.
                :return:
                """
        global masks_train_dic
        file_to_open = "Image Files (*.png *.jpg *.tif)"
        res = QFileDialog.getOpenFileNames(None, "Open File", "/", file_to_open)
        if len(res[0]) > 0:
            # Disable and enable some button
            self.enable_train_msk_btns()
            for img in res[0]:
                if img.split('/')[-1] not in masks_train_dic:
                    # insert into dic
                    masks_train_dic[img.split('/')[-1]] = img
                    # create list item
                    list_item = QtWidgets.QListWidgetItem()
                    list_item.setCheckState(QtCore.Qt.Checked)
                    list_item.setText(img.split('/')[-1])
                    set_stylesheet_listitem(list_item)
                    self.ui.train_mask_lstwdg.addItem(list_item)
                    # update the lcd
                    self.update_train_msk_lcds(1)
        if masks_train_dic and images_train_dic:
            self.ui.train_start_training_btn.setEnabled(True)
        else:
            self.ui.train_start_training_btn.setEnabled(False)

    # Select/Delete images buttons
    def train_selectall_images_lstwdg(self):
        """
        This function is connected to "select all" images button.
        This function change the state of every item in the QListWidget to checked.
        :return:
        """
        for i in range(self.ui.train_image_lstwdg.count()):
            if self.ui.train_image_lstwdg.item(i).checkState() == QtCore.Qt.Unchecked:
                self.ui.train_image_lstwdg.item(i).setCheckState(QtCore.Qt.Checked)

    def train_unselectall_images_lstwdg(self):
        """
        This function is connected to "unselect all" button.
        This function change the state of every item in the QListWidget to unchecked.
        :return:
        """
        for i in range(self.ui.train_image_lstwdg.count()):
            if self.ui.train_image_lstwdg.item(i).checkState() == QtCore.Qt.Checked:
                self.ui.train_image_lstwdg.item(i).setCheckState(QtCore.Qt.Unchecked)

    def train_clear_unselected_images_lstwdg(self):
        """
        This function is connected to "clear selected images" button.
        This function deletes every item in the QListWidget that it's state is checked and also updates
        the LCD and the items in the images_segmentation_dic dic.
        :return:
        """
        global images_train_dic
        delete_lst = []
        for i in range(self.ui.train_image_lstwdg.count()):
            if self.ui.train_image_lstwdg.item(i).checkState() == QtCore.Qt.Unchecked:
                delete_lst.append(self.ui.train_image_lstwdg.item(i))
        for item in delete_lst:
            self.ui.train_image_lstwdg.takeItem(self.ui.train_image_lstwdg.row(item))
            images_train_dic.pop(item.text())
            self.update_train_img_lcds(-1)

    def train_clearimages_lstwdg(self):
        """
        This function is connected to the "clear images" button
        This function deletes every item in the QListWidget, updates the LCD and also images_segmentation_dic.
        :return:
        """
        global images_train_dic
        self.ui.train_image_lstwdg.clear()
        del images_train_dic
        images_train_dic = {}
        self.update_train_img_lcds(0)

    # Select/Delete masks buttons
    def train_selectall_masks_lstwdg(self):
        """
        This function is connected to "select all" images button.
        This function change the state of every item in the QListWidget to checked.
        :return:
        """
        for i in range(self.ui.train_mask_lstwdg.count()):
            if self.ui.train_mask_lstwdg.item(i).checkState() == QtCore.Qt.Unchecked:
                self.ui.train_mask_lstwdg.item(i).setCheckState(QtCore.Qt.Checked)

    def train_unselectall_masks_lstwdg(self):
        """
        This function is connected to "unselect all" button.
        This function change the state of every item in the QListWidget to unchecked.
        :return:
        """
        for i in range(self.ui.train_mask_lstwdg.count()):
            if self.ui.train_mask_lstwdg.item(i).checkState() == QtCore.Qt.Checked:
                self.ui.train_mask_lstwdg.item(i).setCheckState(QtCore.Qt.Unchecked)

    def train_clear_unselected_masks_lstwdg(self):
        """
        This function is connected to "clear selected images" button.
        This function deletes every item in the QListWidget that it's state is checked and also updates
        the LCD and the items in the images_segmentation_dic dic.
        :return:
        """
        global masks_train_dic
        delete_lst = []
        for i in range(self.ui.train_mask_lstwdg.count()):
            if self.ui.train_mask_lstwdg.item(i).checkState() == QtCore.Qt.Unchecked:
                delete_lst.append(self.ui.train_mask_lstwdg.item(i))
        for item in delete_lst:
            self.ui.train_mask_lstwdg.takeItem(self.ui.train_mask_lstwdg.row(item))
            masks_train_dic.pop(item.text())
            self.update_train_msk_lcds(-1)

    def train_clearmasks_lstwdg(self):
        """
        This function is connected to the "clear images" button
        This function deletes every item in the QListWidget, updates the LCD and also images_segmentation_dic.
        :return:
        """
        global masks_train_dic
        self.ui.train_mask_lstwdg.clear()
        del masks_train_dic
        masks_train_dic = {}
        self.update_train_msk_lcds(0)

    def start_training(self):
        if self.ui.train_model_name_txtbox.text() and self.ui.train_epoch_number_txtbox.text():
            self.ui.train_prog_lbl.setText("Training Started")
            model_name = self.ui.train_model_name_txtbox.text()
            num_epochs = int(self.ui.train_epoch_number_txtbox.text())
            batch_size = int(self.ui.train_batchsize_combox.currentText())
            image_batch_size = int(self.ui.train_imagesize_combox.currentText())
            self.ui.train_stop_training_btn.setEnabled(True)
            self.prog_worker = WorkerThread(msg="prog")
            self.prog_worker.start()
            self.prog_worker.update_loader.connect(self.evt_update_loader)
            self.training_Worker = WorkerThread(model=model_name, num_epochs=num_epochs, batch_size=batch_size,
                                                image_batch_size=image_batch_size, msg="train", parent=None)
            self.training_Worker.start()
            self.training_Worker.train_complete.connect(self.evt_train_finished)

    def stop_training(self):
        """
        This function is connected with "Stop Training" button. And it terminates the training thread therefore
        stopping the straining process.
        :return:
        """
        global stop_training_flag
        global training
        stop_training_flag = True
        training = False
        self.ui.train_stop_training_btn.setEnabled(False)
        self.ui.train_prog_lbl.setText("")
        self.ui.train_progbar.setValue(0)

    '''--------------------------------------------Events------------------------------------------------------------'''

    # events
    def evt_update_progress(self, val):
        self.ui.segmentation_progbar.setValue(val)

    def evt_worker_finished(self):
        self.update_progbar_lbl("Successful Segmentation!")
        self.enable_all_segmentation_btns()
        self.ui.segmentation_reset_btn.setEnabled(True)

    def evt_update_progbar_lbl(self, txt):
        self.update_progbar_lbl(txt)

    def evt_update_loader(self, val):
        self.ui.train_progbar.setValue(val)

    def evt_train_finished(self, acc, modelname):
        self.ui.train_progbar.setValue(100)
        self.ui.train_prog_lbl.setText("Training Complete! Model Accuracy: " + acc + "%")
        data = pd.read_csv('Models/Models.csv')
        today = date.today()
        data.loc[len(data.index)] = [today.strftime("%d/%m/%Y"), modelname, acc]
        data.to_csv('Models/Models.csv', index=False)

    '''--------------------------------------------Help functions----------------------------------------------------'''

    # Help functions
    def disable_all_segmentation_btns(self):
        """
        This is a help function that disables all buttons that shouldn't be used without any images uploaded.
        :return:
        """
        self.ui.segmentation_start_segmentation_btn.setEnabled(False)
        self.ui.segmentation_stop_segmentation_btn.setEnabled(False)
        self.ui.segmentation_show_results_btn.setEnabled(False)
        self.ui.segmentation_downloadresults_btn.setEnabled(False)
        self.ui.segmentation_selectall_btn.setEnabled(False)
        self.ui.segmentation_clear_unselect_images_btn.setEnabled(False)
        self.ui.segmentation_unselectall_btn.setEnabled(False)
        self.ui.segmentation_clearimages_btn.setEnabled(False)

    def enable_all_segmentation_btns(self):
        """
        This is a help function that enable all buttons that disable_all_btns help function disables.
        :return:
        """
        self.ui.segmentation_start_segmentation_btn.setEnabled(True)
        self.ui.segmentation_stop_segmentation_btn.setEnabled(True)
        self.ui.segmentation_show_results_btn.setEnabled(True)
        self.ui.segmentation_downloadresults_btn.setEnabled(True)
        self.ui.segmentation_selectall_btn.setEnabled(True)
        self.ui.segmentation_clear_unselect_images_btn.setEnabled(True)
        self.ui.segmentation_unselectall_btn.setEnabled(True)
        self.ui.segmentation_clearimages_btn.setEnabled(True)

    def disable_all_train_btns(self):
        # Disable images
        self.disable_train_img_btns()

        # Disable masks
        self.disable_train_msk_btns()

        # Disable the rest of buttons
        self.ui.train_start_training_btn.setEnabled(False)
        self.ui.train_stop_training_btn.setEnabled(False)

    def disable_train_img_btns(self):
        """
        This help functions disables all buttons who controls the image QListWidget.
        :return:
        """
        self.ui.train_image_unselectall_btn.setEnabled(False)
        self.ui.train_clearimages_btn.setEnabled(False)
        self.ui.train_clear_unselect_images_btn.setEnabled(False)
        self.ui.train_image_selectall_btn.setEnabled(False)

    def disable_train_msk_btns(self):
        """
        This help functions disables all buttons who controls the image QListWidget.
        :return:
        """
        self.ui.train_unselectall_masks_btn.setEnabled(False)
        self.ui.train_clear_unselect_masks_btn.setEnabled(False)
        self.ui.train_cleamasks_btn.setEnabled(False)
        self.ui.train_selectall_masks_btn.setEnabled(False)

    def enable_all_train_btns(self):

        # Enable images buttons
        self.enable_train_img_btns()

        # Enable masks buttons
        self.enable_train_msk_btns()

    def enable_train_img_btns(self):
        """
        This help functions enables all buttons who controls the image QListWidget.
        :return:
        """
        self.ui.train_image_unselectall_btn.setEnabled(True)
        self.ui.train_clearimages_btn.setEnabled(True)
        self.ui.train_clear_unselect_images_btn.setEnabled(True)
        self.ui.train_image_selectall_btn.setEnabled(True)

    def enable_train_msk_btns(self):
        """
        This help functions enables all buttons who controls the image QListWidget.
        :return:
        """
        self.ui.train_unselectall_masks_btn.setEnabled(True)
        self.ui.train_clear_unselect_masks_btn.setEnabled(True)
        self.ui.train_cleamasks_btn.setEnabled(True)
        self.ui.train_selectall_masks_btn.setEnabled(True)

    def update_lcds(self, item):
        """
        This function is a help function wich updates the lcd and also disables the buttons when there is no images left

        :param item:
        item is int :
            item > 0: The function will increase one from the LCD.
            item < 0: The function will decrease one from the LCD and checks if it's 0,
                                                                            If it is then all buttons will be disabled.
            item = 0: The function will reset the LCD and disable all buttons.
        item is QListWidgetItem:
        It updates the LCD.
        :return:
        """
        global num_segmentation_selected_images
        global num_segmentation_unselected_images

        if type(item) == int:
            if item > 0:
                num_segmentation_selected_images += 1
                self.ui.segmentaion_selected_lcd.display(num_segmentation_selected_images)

            elif item < 0:
                num_segmentation_unselected_images -= 1
                self.ui.segmentation_unselected_lcd.display(num_segmentation_unselected_images)
                if self.ui.segmentation_image_lstwdg.count() == 0:
                    self.disable_all_segmentation_btns()
                    self.disable_all_segmentation_btns()
                    self.ui.segmentation_image_lbl.setText("Please insert image to view on the screen")
            elif item == 0:
                num_segmentation_selected_images = 0
                num_segmentation_unselected_images = 0
                self.ui.segmentaion_selected_lcd.display(num_segmentation_selected_images)
                self.ui.segmentation_unselected_lcd.display(num_segmentation_unselected_images)
                self.disable_all_segmentation_btns()
                self.ui.segmentation_image_lbl.setText("Please insert image to view on the screen")

        else:
            if item.checkState():
                num_segmentation_unselected_images -= 1
                num_segmentation_selected_images += 1
                self.ui.segmentaion_selected_lcd.display(num_segmentation_selected_images)
                self.ui.segmentation_unselected_lcd.display(num_segmentation_unselected_images)
            else:
                num_segmentation_unselected_images += 1
                num_segmentation_selected_images -= 1
                self.ui.segmentaion_selected_lcd.display(num_segmentation_selected_images)
                self.ui.segmentation_unselected_lcd.display(num_segmentation_unselected_images)

    def update_train_img_lcds(self, item):
        """
        This function is a help function which updates the lcd and also disables the buttons when there is no images left

        :param item:
        item is int :
            item > 0: The function will increase one from the LCD.
            item < 0: The function will decrease one from the LCD and checks if it's 0,
                                                                            If it is then all buttons will be disabled.
            item = 0: The function will reset the LCD and disable all buttons.
        item is QListWidgetItem:
        It updates the LCD.
        :return:
        """
        global num_train_selected_images
        global num_train_unselected_images

        if type(item) == int:
            if item > 0:
                num_train_selected_images += 1
                self.ui.train_selected_images_lcd.display(num_train_selected_images)

            elif item < 0:
                num_train_unselected_images -= 1
                self.ui.train_unselected_images_lcd.display(num_train_unselected_images)
                if self.ui.train_image_lstwdg.count() == 0:
                    self.disable_train_img_btns()
            elif item == 0:
                num_train_selected_images = 0
                num_train_unselected_images = 0
                self.ui.train_selected_images_lcd.display(num_train_selected_images)
                self.ui.train_unselected_images_lcd.display(num_train_unselected_images)
                self.disable_train_img_btns()

        else:
            if item.checkState():
                num_train_unselected_images -= 1
                num_train_selected_images += 1
                self.ui.train_selected_images_lcd.display(num_train_selected_images)
                self.ui.train_unselected_images_lcd.display(num_train_unselected_images)
            else:
                num_train_unselected_images += 1
                num_train_selected_images -= 1
                self.ui.train_selected_images_lcd.display(num_train_selected_images)
                self.ui.train_unselected_images_lcd.display(num_train_unselected_images)

    def update_train_msk_lcds(self, item):
        """
        This function is a help function which updates the lcd and also disables the buttons when there is no images left

        :param item:
        item is int :
            item > 0: The function will increase one from the LCD.
            item < 0: The function will decrease one from the LCD and checks if it's 0,
                                                                            If it is then all buttons will be disabled.
            item = 0: The function will reset the LCD and disable all buttons.
        item is QListWidgetItem:
        It updates the LCD.
        :return:
        """
        global num_train_selected_masks
        global num_train_unselected_masks

        if type(item) == int:
            if item > 0:
                num_train_selected_masks += 1
                self.ui.train_selected_masks_lcd.display(num_train_selected_masks)

            elif item < 0:
                num_train_unselected_masks -= 1
                self.ui.train_unselected_masks_lcd.display(num_train_unselected_masks)
                if self.ui.train_image_lstwdg.count() == 0:
                    self.disable_train_img_btns()
            elif item == 0:
                num_train_selected_masks = 0
                num_train_unselected_masks = 0
                self.ui.train_selected_masks_lcd.display(num_train_selected_masks)
                self.ui.train_unselected_masks_lcd.display(num_train_unselected_masks)
                self.disable_train_img_btns()

        else:
            if item.checkState() == QtCore.Qt.Checked:
                num_train_unselected_masks -= 1
                num_train_selected_masks += 1
                self.ui.train_selected_masks_lcd.display(num_train_selected_masks)
                self.ui.train_unselected_masks_lcd.display(num_train_unselected_masks)
            else:
                num_train_unselected_masks += 1
                num_train_selected_masks -= 1
                self.ui.train_selected_masks_lcd.display(num_train_selected_masks)
                self.ui.train_unselected_masks_lcd.display(num_train_unselected_masks)

    def show_image(self, item):
        """
        This function updates the images label with the image in the index item (the first image).
        :param item: The QListWidgetItem to set the image.
        :return:
        """
        global images_segmentation_dic
        pixmap = QPixmap(images_segmentation_dic[item.text()])
        pixmap = pixmap.scaled(512, 512, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.segmentation_image_lbl.setPixmap(pixmap)
        # self.ui.segmentation_image_lbl.setPixmap(QPixmap(images_segmentation_dic[item.text()]))

    def update_progbar_lbl(self, txt):
        """
        This help function updates the label underneath the progress bar that gives information about the segmentation.
        :param txt: String to update the label to.
        :return:
        """
        self.ui.segmentation_info_progbar_lbl.setText(txt)

    def setup_temp(self):
        """
        This is a help function. it removes any files left in the temp directory.
        :return:
        """
        onlyfiles = [f for f in listdir("temp") if isfile(join("temp", f))]
        if onlyfiles:
            for f in onlyfiles:
                os.remove("temp/" + f)


'''--------------------------------------------- Segmented images CLASS --------------------------------------------'''


class Segmented_images(QMainWindow):
    def __init__(self, parent=None):
        super(Segmented_images, self).__init__(parent)
        global segmented_images_dic
        self.ui = Ui_Segmented_images()
        self.ui.setupUi(self)
        self.segmented_lst = list(segmented_images_dic.keys())
        self.setup_first_image()

        # Parameters
        self.index = 0

        # Buttons
        # Next image
        self.ui.showimage_next_btn.clicked.connect(self.next_image)
        self.ui.showimage_previous_btn.clicked.connect(self.previous_image)

    def setup_first_image(self):
        """
        This function setup the first image
        :return:
        """
        pixmap = QPixmap("temp/" + self.segmented_lst[0])
        pixmap = pixmap.scaled(1011, 741, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.image_lbl.setPixmap(pixmap)

    def next_image(self):
        """
        This functions gets the next segmented image from temp file
        :return:
        """
        self.index += 1
        if self.index == len(self.segmented_lst):
            self.index = 0
        pixmap = QPixmap("temp/" + self.segmented_lst[self.index])
        pixmap = pixmap.scaled(1011, 741, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.image_lbl.setPixmap(pixmap)

    def previous_image(self):
        """
        This function gets the previous segmented image from temp file
        :return:
        """
        self.index -= 1
        if self.index == -1:
            self.index = len(self.segmented_lst) - 1
        pixmap = QPixmap("temp/" + self.segmented_lst[self.index])
        pixmap = pixmap.scaled(1011, 741, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.image_lbl.setPixmap(pixmap)


class CustomCallback(keras.callbacks.Callback):
    def on_train_batch_end(self, batch, logs=None):
        keys = list(logs.keys())
        print('value of model.stop_training:%s' % (self.model.stop_training))
        if stop_training_flag:
            print('stop training on batch %s' % (batch))
            self.model.stop_training = True
            return

    # def on_epoch_end(self, epoch, logs=None):
    #     keys = list(logs.keys())
    #     print("End epoch {} of training; got log keys: {}".format(epoch, keys))
    #     worker = WorkerThread(msg="emit_prog", num_epochs=epoch)
    #     worker.start()


# Thread Class
class WorkerThread(QtCore.QThread):
    def __init__(self, model="", msg="", num_epochs=10, batch_size=4, image_batch_size=256, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.model = model
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.image_batch_size = image_batch_size
        self.msg = msg

    # QCore QThread Signal
    update_progress = QtCore.pyqtSignal(int)
    worker_complete = QtCore.pyqtSignal(object)
    progbar_lbl_update = QtCore.pyqtSignal(object)
    update_loader = QtCore.pyqtSignal(int)
    train_complete = QtCore.pyqtSignal(object, object)

    def run_segmentation(self):
        print("---------------------------Start Testing--------------------------------")
        global images_segmentation_dic
        global segmented_images_dic
        loaded_model = load_model("Models/" + self.model)
        prog_bar_counter = 1
        self.progbar_lbl_update.emit("Segmentation Started")

        for key in images_segmentation_dic:
            val = images_segmentation_dic[key]
            path = val

            img = cv2.imread(val, 0) / 255
            imgwidth, imgheight = img.shape

            if imgwidth % BATCH_WIDTH != 0 and imgheight % BATCH_HIGHT != 0:
                img = cv2.resize(img, (imgheight - (imgheight % BATCH_HIGHT), imgwidth - (imgwidth % BATCH_WIDTH)))
            elif imgheight % BATCH_HIGHT != 0:
                img = cv2.resize(img, (imgheight - (imgheight % BATCH_HIGHT), imgwidth))
            elif imgwidth % BATCH_WIDTH != 0:
                img = cv2.resize(img, (imgheight, imgwidth - (imgwidth % BATCH_WIDTH)))

            imgwidth, imgheight = img.shape
            number_of_patches = (imgheight / BATCH_HIGHT) * (imgheight / BATCH_HIGHT)
            counter = 1
            if self.msg == "segmentation":
                segmintated = np.zeros((imgheight, imgwidth), dtype=np.uint8)
            else:
                segmintated = np.zeros((imgheight, imgwidth), dtype=np.float32)
            indexheight = imgheight
            indexwidth = imgwidth
            for i in tqdm(range(0, indexheight , BATCH_HIGHT)):
                for j in tqdm(range(0, indexwidth , BATCH_WIDTH)):
                    info = "Image Name: " + key + " " + str(counter) + " OF " + str(number_of_patches)
                    self.progbar_lbl_update.emit(info)
                    counter += 1
                    patch = img[j:j + BATCH_WIDTH, i:i + BATCH_HIGHT]
                    if len(patch.shape) == 3:
                        patch = patch[:, :, :3]
                    patch = np.expand_dims(patch, axis=-1)
                    patch = np.expand_dims(patch, axis=0)
                    prediction = loaded_model.predict(patch)
                    prediction = prediction[0]
                    # The binarization will only work if the raw image check box is off
                    if self.msg == "segmentation":
                        prediction = contrastStretching(prediction)
                        prediction = otsu_threholding(prediction)
                        prediction = gaussian_filter(prediction, sigma=0.4)

                        prediction[prediction >= 1] = 255
                        prediction[prediction < 1] = 0
                        prediction = prediction.astype(np.uint8)
                    for k in range(BATCH_HIGHT):
                        for z in range(BATCH_WIDTH):
                            segmintated[j + k][i + z] = prediction[k][z]

                    # setting value to progress bar
                    prog_bar_counter += 100 / (number_of_patches * len(images_segmentation_dic))

                    # self.update_progress.emit(prog_bar_counter)
                    self.update_progress.emit(prog_bar_counter)
                    indexwidth = indexwidth - BATCH_WIDTH
                indexwidth = imgwidth
                indexheight = indexheight - BATCH_HIGHT
            _, tail = ntpath.split(path)
            segmented_images_dic[tail] = np.asarray(segmintated)
            if self.msg == "segmentation":
                cv2.imwrite('temp/' + tail, segmintated)

        self.update_progress.emit(100)
        self.worker_complete.emit(segmented_images_dic)

    def run_train(self):
        global training
        global stop_training_flag
        print("---------------------------Start Training--------------------------------")
        # Update batch size
        update_batch_size(self.image_batch_size)

        images, maskes = preprocessImage()
        x_train, x_test, y_train, y_test = train_test_split(images, maskes, test_size=0.2)

        model = uNet()
        # simple early stopping
        es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
        # fit model
        results = model.fit(x_train, y_train, epochs=self.num_epochs, batch_size=self.batch_size
                            , validation_split=0.1, verbose=1, callbacks=[es, CustomCallback()])

        # To stop the process of training if the stop button is pressed
        if stop_training_flag:
            stop_training_flag = False
        else:
            # evaluate
            score, accuracy = model.evaluate(x_test, y_test, batch_size=self.batch_size)
            # the results
            print("Our Models' Score = {:.2f}".format(score))
            print("The Accuracy of the model = {:.2f}".format(accuracy * 100))

            # after Evaluating we save the model and the weights into the .h5 file
            print("--- saving the model ---")

            if self.image_batch_size == 256:
                model.save('Models/256/' + self.model + ".h5")
            else:
                model.save('Models/512/' + self.model + ".h5")
        self.train_complete.emit(str(accuracy * 100), self.model)
        training = False

    def run_loader(self):
        global training
        counter = 0
        while (training):
            counter += 10
            if counter > 100:
                counter = 1
            self.update_loader.emit(counter)
            self.sleep(1)

    def run(self):
        if self.msg == "segmentation" or self.msg == "segmentation_raw":
            self.run_segmentation()
        elif self.msg == "train":
            self.run_train()
        elif self.msg == "prog":
            self.run_loader()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
