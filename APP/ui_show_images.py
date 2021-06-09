# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_images_windowtTAsUu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class Ui_Segmented_images(object):
    def setupUi(self, Segmented_images):
        if not Segmented_images.objectName():
            Segmented_images.setObjectName(u"Segmented_images")
        Segmented_images.resize(1084, 864)
        self.setWindowIcon(QtGui.QIcon(u'icons/24x24/app_icon3_1'))

        self.centralwidget = QWidget(Segmented_images)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.image_lbl = QLabel(self.frame)
        self.image_lbl.setObjectName(u"image_lbl")
        self.image_lbl.setGeometry(QRect(30, 10, 1011, 741))
        self.image_lbl.setAlignment(Qt.AlignCenter)
        self.showimage_btns_frame = QFrame(self.frame)
        self.showimage_btns_frame.setObjectName(u"showimage_btns_frame")
        self.showimage_btns_frame.setGeometry(QRect(390, 760, 291, 41))
        self.showimage_btns_frame.setStyleSheet(u"QFrame {\n"
"    \n"
"	background-color: rgb(89,89, 89);\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 14px;\n"
"\n"
"}\n"
"")
        self.showimage_previous_btn = QPushButton(self.showimage_btns_frame)
        self.showimage_previous_btn.setObjectName(u"showimage_previous_btn")
        self.showimage_previous_btn.setGeometry(QRect(15, 5, 121, 31))
        self.showimage_previous_btn.setStyleSheet(u"QPushButton {\n"
"    \n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"C:/Users/loai0/PycharmProjects/pythonProject6/icons/24x24/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showimage_previous_btn.setIcon(icon)
        self.showimage_previous_btn.setIconSize(QSize(24, 24))
        self.showimage_next_btn = QPushButton(self.showimage_btns_frame)
        self.showimage_next_btn.setObjectName(u"showimage_next_btn")
        self.showimage_next_btn.setGeometry(QRect(165, 5, 111, 31))
        self.showimage_next_btn.setStyleSheet(u"QPushButton {\n"
"    \n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/loai0/PycharmProjects/pythonProject6/icons/24x24/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showimage_next_btn.setIcon(icon1)
        self.showimage_next_btn.setIconSize(QSize(24, 24))
        self.showimage_rights_lbl = QLabel(self.frame)
        self.showimage_rights_lbl.setObjectName(u"showimage_rights_lbl")
        self.showimage_rights_lbl.setGeometry(QRect(360, 810, 361, 21))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.showimage_rights_lbl.setFont(font)
        self.showimage_rights_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.frame)

        Segmented_images.setCentralWidget(self.centralwidget)

        self.retranslateUi(Segmented_images)

        QMetaObject.connectSlotsByName(Segmented_images)
    # setupUi

    def retranslateUi(self, Segmented_images):
        Segmented_images.setWindowTitle(QCoreApplication.translate("Segmented_images", u"MainWindow", None))
        self.image_lbl.setText("")
        self.showimage_previous_btn.setText(QCoreApplication.translate("Segmented_images", u" Previous", None))
        self.showimage_next_btn.setText(QCoreApplication.translate("Segmented_images", u" Next", None))
        self.showimage_rights_lbl.setText(QCoreApplication.translate("Segmented_images", u"Developed By Loai Ab & Moataz Ata  \u00a9\ufe0f 2021 All rights reserved", None))
    # retranslateUi

