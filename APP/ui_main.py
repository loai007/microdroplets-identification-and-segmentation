# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiTpNXDJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1326, 824)
        MainWindow.setWindowIcon(QtGui.QIcon(u'icons/24x24/app_icon3_1'))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1300, 500))
        MainWindow.setMaximumSize(QSize(1500, 1500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(100, 0))
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: #FFFF;\n"
"")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy1)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u"icons/24x24/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(40, 40))

        self.verticalLayout_9.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy2)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(130, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_top_menus.sizePolicy().hasHeightForWidth())
        self.frame_top_menus.setSizePolicy(sizePolicy3)
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.segmentation_page_btn = QPushButton(self.frame_top_menus)
        self.segmentation_page_btn.setObjectName(u"segmentation_page_btn")
        self.segmentation_page_btn.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"Aharoni")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.segmentation_page_btn.setFont(font)
        self.segmentation_page_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.segmentation_page_btn)

        self.training_page_btn = QPushButton(self.frame_top_menus)
        self.training_page_btn.setObjectName(u"training_page_btn")
        self.training_page_btn.setMinimumSize(QSize(0, 40))
        self.training_page_btn.setFont(font)
        self.training_page_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.training_page_btn)

        self.help_page_btn = QPushButton(self.frame_top_menus)
        self.help_page_btn.setObjectName(u"help_page_btn")
        self.help_page_btn.setMinimumSize(QSize(0, 40))
        self.help_page_btn.setFont(font)
        self.help_page_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.help_page_btn)

        self.about_page_btn = QPushButton(self.frame_top_menus)
        self.about_page_btn.setObjectName(u"about_page_btn")
        self.about_page_btn.setMinimumSize(QSize(0, 40))
        self.about_page_btn.setFont(font)
        self.about_page_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.about_page_btn)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_14)


        self.verticalLayout_3.addWidget(self.frame_top_menus)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(1300, 800))
        self.segmentation_page = QWidget()
        self.segmentation_page.setObjectName(u"segmentation_page")
        self.verticalLayout_7 = QVBoxLayout(self.segmentation_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.segmentation_down_Frame = QFrame(self.segmentation_page)
        self.segmentation_down_Frame.setObjectName(u"segmentation_down_Frame")
        self.segmentation_down_Frame.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.segmentation_down_Frame.sizePolicy().hasHeightForWidth())
        self.segmentation_down_Frame.setSizePolicy(sizePolicy3)
        self.segmentation_down_Frame.setMinimumSize(QSize(0, 0))
        self.segmentation_down_Frame.setFrameShape(QFrame.StyledPanel)
        self.segmentation_down_Frame.setFrameShadow(QFrame.Raised)
        self.segmentation_buttons_frame = QFrame(self.segmentation_down_Frame)
        self.segmentation_buttons_frame.setObjectName(u"segmentation_buttons_frame")
        self.segmentation_buttons_frame.setGeometry(QRect(0, 530, 1161, 171))
        self.segmentation_buttons_frame.setStyleSheet(u"\n"
"background-color: rgb(89, 89, 89);")
        self.segmentation_progbar = QProgressBar(self.segmentation_buttons_frame)
        self.segmentation_progbar.setObjectName(u"segmentation_progbar")
        self.segmentation_progbar.setGeometry(QRect(210, 110, 761, 20))
        sizePolicy3.setHeightForWidth(self.segmentation_progbar.sizePolicy().hasHeightForWidth())
        self.segmentation_progbar.setSizePolicy(sizePolicy3)
        self.segmentation_progbar.setMinimumSize(QSize(20, 20))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.segmentation_progbar.setFont(font1)
        self.segmentation_progbar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-width: 2px;\n"
"	border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 14px;\n"
"	color: white;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #CD96CD;\n"
"	border-radius: 10px\n"
"}")
        self.segmentation_progbar.setValue(0)
        self.segmentation_progbar.setAlignment(Qt.AlignCenter)
        self.segmentation_progbar.setTextVisible(True)
        self.horizontalLayoutWidget = QWidget(self.segmentation_buttons_frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 1111, 41))
        self.segmentation_main_buttons_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.segmentation_main_buttons_layout.setObjectName(u"segmentation_main_buttons_layout")
        self.segmentation_main_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.segmentation_browse_btn = QPushButton(self.horizontalLayoutWidget)
        self.segmentation_browse_btn.setObjectName(u"segmentation_browse_btn")
        sizePolicy.setHeightForWidth(self.segmentation_browse_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_browse_btn.setSizePolicy(sizePolicy)
        self.segmentation_browse_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_browse_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_browse_btn.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u"icons/24x24/cil-image-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_browse_btn.setIcon(icon1)
        self.segmentation_browse_btn.setIconSize(QSize(24, 24))

        self.segmentation_main_buttons_layout.addWidget(self.segmentation_browse_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.segmentation_main_buttons_layout.addItem(self.horizontalSpacer)

        self.segmentation_start_segmentation_btn = QPushButton(self.horizontalLayoutWidget)
        self.segmentation_start_segmentation_btn.setObjectName(u"segmentation_start_segmentation_btn")
        sizePolicy.setHeightForWidth(self.segmentation_start_segmentation_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_start_segmentation_btn.setSizePolicy(sizePolicy)
        self.segmentation_start_segmentation_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_start_segmentation_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_start_segmentation_btn.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u"icons/24x24/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_start_segmentation_btn.setIcon(icon2)
        self.segmentation_start_segmentation_btn.setIconSize(QSize(24, 24))

        self.segmentation_main_buttons_layout.addWidget(self.segmentation_start_segmentation_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.segmentation_main_buttons_layout.addItem(self.horizontalSpacer_2)

        self.segmentation_stop_segmentation_btn = QPushButton(self.horizontalLayoutWidget)
        self.segmentation_stop_segmentation_btn.setObjectName(u"segmentation_stop_segmentation_btn")
        sizePolicy.setHeightForWidth(self.segmentation_stop_segmentation_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_stop_segmentation_btn.setSizePolicy(sizePolicy)
        self.segmentation_stop_segmentation_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_stop_segmentation_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_stop_segmentation_btn.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u"icons/24x24/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_stop_segmentation_btn.setIcon(icon3)
        self.segmentation_stop_segmentation_btn.setIconSize(QSize(24, 24))

        self.segmentation_main_buttons_layout.addWidget(self.segmentation_stop_segmentation_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.segmentation_main_buttons_layout.addItem(self.horizontalSpacer_3)

        self.segmentation_show_results_btn = QPushButton(self.horizontalLayoutWidget)
        self.segmentation_show_results_btn.setObjectName(u"segmentation_show_results_btn")
        sizePolicy.setHeightForWidth(self.segmentation_show_results_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_show_results_btn.setSizePolicy(sizePolicy)
        self.segmentation_show_results_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_show_results_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_show_results_btn.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u"icons/24x24/cil-screen-desktop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_show_results_btn.setIcon(icon4)
        self.segmentation_show_results_btn.setIconSize(QSize(24, 24))

        self.segmentation_main_buttons_layout.addWidget(self.segmentation_show_results_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.segmentation_main_buttons_layout.addItem(self.horizontalSpacer_4)

        self.segmentation_downloadresults_btn = QPushButton(self.horizontalLayoutWidget)
        self.segmentation_downloadresults_btn.setObjectName(u"segmentation_downloadresults_btn")
        sizePolicy.setHeightForWidth(self.segmentation_downloadresults_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_downloadresults_btn.setSizePolicy(sizePolicy)
        self.segmentation_downloadresults_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_downloadresults_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_downloadresults_btn.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(u"icons/24x24/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_downloadresults_btn.setIcon(icon5)
        self.segmentation_downloadresults_btn.setIconSize(QSize(24, 24))

        self.segmentation_main_buttons_layout.addWidget(self.segmentation_downloadresults_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.segmentation_main_buttons_layout.addItem(self.horizontalSpacer_10)

        self.segmentation_reset_btn = QPushButton(self.horizontalLayoutWidget)
        self.segmentation_reset_btn.setObjectName(u"segmentation_reset_btn")
        sizePolicy.setHeightForWidth(self.segmentation_reset_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_reset_btn.setSizePolicy(sizePolicy)
        self.segmentation_reset_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_reset_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_reset_btn.setStyleSheet(u"QPushButton {\n"
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
        icon6 = QIcon()
        icon6.addFile(u"C:/Users/loai0/PycharmProjects/pythonProject6/icons/24x24/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_reset_btn.setIcon(icon6)
        self.segmentation_reset_btn.setIconSize(QSize(24, 24))

        self.segmentation_main_buttons_layout.addWidget(self.segmentation_reset_btn)

        self.segmentation_info_progbar_lbl = QLabel(self.segmentation_buttons_frame)
        self.segmentation_info_progbar_lbl.setObjectName(u"segmentation_info_progbar_lbl")
        self.segmentation_info_progbar_lbl.setGeometry(QRect(316, 140, 581, 20))
        font2 = QFont()
        font2.setFamily(u"Arial Narrow")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.segmentation_info_progbar_lbl.setFont(font2)
        self.segmentation_info_progbar_lbl.setStyleSheet(u"")
        self.segmentation_info_progbar_lbl.setAlignment(Qt.AlignCenter)
        self.segmentation_image_lbl = QLabel(self.segmentation_down_Frame)
        self.segmentation_image_lbl.setObjectName(u"segmentation_image_lbl")
        self.segmentation_image_lbl.setGeometry(QRect(620, 0, 512, 512))
        font3 = QFont()
        font3.setFamily(u"Aharoni")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.segmentation_image_lbl.setFont(font3)
        self.segmentation_image_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.segmentation_image_lbl.setAlignment(Qt.AlignCenter)
        self.segmentation_image_lstwdg = QListWidget(self.segmentation_down_Frame)
        self.segmentation_image_lstwdg.setObjectName(u"segmentation_image_lstwdg")
        self.segmentation_image_lstwdg.setGeometry(QRect(20, 30, 341, 441))
        self.segmentation_image_lstwdg.setStyleSheet(u"background-color: rgb(88, 88, 88);")
        self.rights_lbl = QLabel(self.segmentation_down_Frame)
        self.rights_lbl.setObjectName(u"rights_lbl")
        self.rights_lbl.setGeometry(QRect(410, 704, 431, 21))
        font4 = QFont()
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setWeight(75)
        font4.setStrikeOut(False)
        self.rights_lbl.setFont(font4)
        self.rights_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QWidget(self.segmentation_down_Frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(380, 390, 227, 62))
        self.segmentation_selected_layout = QGridLayout(self.gridLayoutWidget)
        self.segmentation_selected_layout.setObjectName(u"segmentation_selected_layout")
        self.segmentation_selected_layout.setContentsMargins(0, 0, 0, 0)
        self.segmentation_unselected_lcd = QLCDNumber(self.gridLayoutWidget)
        self.segmentation_unselected_lcd.setObjectName(u"segmentation_unselected_lcd")

        self.segmentation_selected_layout.addWidget(self.segmentation_unselected_lcd, 2, 1, 1, 1)

        self.segmentation_selected_images_lbl = QLabel(self.gridLayoutWidget)
        self.segmentation_selected_images_lbl.setObjectName(u"segmentation_selected_images_lbl")
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.segmentation_selected_images_lbl.setFont(font5)
        self.segmentation_selected_images_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.segmentation_selected_layout.addWidget(self.segmentation_selected_images_lbl, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.segmentation_selected_layout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.segmentation_unselected_images_lbl = QLabel(self.gridLayoutWidget)
        self.segmentation_unselected_images_lbl.setObjectName(u"segmentation_unselected_images_lbl")
        self.segmentation_unselected_images_lbl.setFont(font5)
        self.segmentation_unselected_images_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.segmentation_selected_layout.addWidget(self.segmentation_unselected_images_lbl, 2, 0, 1, 1)

        self.segmentaion_selected_lcd = QLCDNumber(self.gridLayoutWidget)
        self.segmentaion_selected_lcd.setObjectName(u"segmentaion_selected_lcd")

        self.segmentation_selected_layout.addWidget(self.segmentaion_selected_lcd, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.segmentation_selected_layout.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.verticalLayoutWidget = QWidget(self.segmentation_down_Frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(400, 180, 190, 197))
        self.segmentation_lstimages_bntlayout = QVBoxLayout(self.verticalLayoutWidget)
        self.segmentation_lstimages_bntlayout.setObjectName(u"segmentation_lstimages_bntlayout")
        self.segmentation_lstimages_bntlayout.setContentsMargins(0, 0, 0, 0)
        self.segmentation_selectall_btn = QPushButton(self.verticalLayoutWidget)
        self.segmentation_selectall_btn.setObjectName(u"segmentation_selectall_btn")
        sizePolicy.setHeightForWidth(self.segmentation_selectall_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_selectall_btn.setSizePolicy(sizePolicy)
        self.segmentation_selectall_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_selectall_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_selectall_btn.setFont(font1)
        self.segmentation_selectall_btn.setAutoFillBackground(False)
        self.segmentation_selectall_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/24x24/cil-task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_selectall_btn.setIcon(icon7)
        self.segmentation_selectall_btn.setIconSize(QSize(24, 24))

        self.segmentation_lstimages_bntlayout.addWidget(self.segmentation_selectall_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.segmentation_lstimages_bntlayout.addItem(self.verticalSpacer_3)

        self.segmentation_unselectall_btn = QPushButton(self.verticalLayoutWidget)
        self.segmentation_unselectall_btn.setObjectName(u"segmentation_unselectall_btn")
        sizePolicy.setHeightForWidth(self.segmentation_unselectall_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_unselectall_btn.setSizePolicy(sizePolicy)
        self.segmentation_unselectall_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_unselectall_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_unselectall_btn.setFont(font1)
        self.segmentation_unselectall_btn.setAutoFillBackground(False)
        self.segmentation_unselectall_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_unselectall_btn.setIcon(icon8)
        self.segmentation_unselectall_btn.setIconSize(QSize(24, 24))

        self.segmentation_lstimages_bntlayout.addWidget(self.segmentation_unselectall_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.segmentation_lstimages_bntlayout.addItem(self.verticalSpacer_4)

        self.segmentation_clear_unselect_images_btn = QPushButton(self.verticalLayoutWidget)
        self.segmentation_clear_unselect_images_btn.setObjectName(u"segmentation_clear_unselect_images_btn")
        sizePolicy.setHeightForWidth(self.segmentation_clear_unselect_images_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_clear_unselect_images_btn.setSizePolicy(sizePolicy)
        self.segmentation_clear_unselect_images_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_clear_unselect_images_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_clear_unselect_images_btn.setFont(font1)
        self.segmentation_clear_unselect_images_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.segmentation_clear_unselect_images_btn.setIcon(icon8)
        self.segmentation_clear_unselect_images_btn.setIconSize(QSize(24, 24))

        self.segmentation_lstimages_bntlayout.addWidget(self.segmentation_clear_unselect_images_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.segmentation_lstimages_bntlayout.addItem(self.verticalSpacer_2)

        self.segmentation_clearimages_btn = QPushButton(self.verticalLayoutWidget)
        self.segmentation_clearimages_btn.setObjectName(u"segmentation_clearimages_btn")
        sizePolicy.setHeightForWidth(self.segmentation_clearimages_btn.sizePolicy().hasHeightForWidth())
        self.segmentation_clearimages_btn.setSizePolicy(sizePolicy)
        self.segmentation_clearimages_btn.setMinimumSize(QSize(0, 31))
        self.segmentation_clearimages_btn.setMaximumSize(QSize(10000, 10000))
        self.segmentation_clearimages_btn.setFont(font1)
        self.segmentation_clearimages_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"icons/24x24/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segmentation_clearimages_btn.setIcon(icon9)
        self.segmentation_clearimages_btn.setIconSize(QSize(24, 24))

        self.segmentation_lstimages_bntlayout.addWidget(self.segmentation_clearimages_btn)

        self.models_QComboBox = QComboBox(self.segmentation_down_Frame)
        self.models_QComboBox.setObjectName(u"models_QComboBox")
        self.models_QComboBox.setGeometry(QRect(390, 30, 171, 38))
        font6 = QFont()
        font6.setFamily(u"Aharoni")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(9)
        self.models_QComboBox.setFont(font6)
        self.models_QComboBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.models_QComboBox.setLayoutDirection(Qt.LeftToRight)
        self.models_QComboBox.setStyleSheet(u"border-style: outset;\n"
"border-width: 3px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Aharoni\";\n"
"border-radius: 9px;\n"
"border-color: rgb(66, 66, 66);\n"
"padding-left: 10px;")
        self.formLayoutWidget_2 = QWidget(self.segmentation_down_Frame)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(383, 80, 221, 90))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_15)

        self.segmentation_imagesize_lbl = QLabel(self.formLayoutWidget_2)
        self.segmentation_imagesize_lbl.setObjectName(u"segmentation_imagesize_lbl")
        self.segmentation_imagesize_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.segmentation_imagesize_lbl)

        self.segmentation_batchsize_256_radbtn = QRadioButton(self.formLayoutWidget_2)
        self.segmentation_batchsize_256_radbtn.setObjectName(u"segmentation_batchsize_256_radbtn")
        self.segmentation_batchsize_256_radbtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Aharoni\";")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.segmentation_batchsize_256_radbtn)

        self.segmentation_batchsize_512_radbtn = QRadioButton(self.formLayoutWidget_2)
        self.segmentation_batchsize_512_radbtn.setObjectName(u"segmentation_batchsize_512_radbtn")
        self.segmentation_batchsize_512_radbtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Aharoni\";")
        self.segmentation_batchsize_512_radbtn.setChecked(True)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.segmentation_batchsize_512_radbtn)

        self.segmentation_rawimg_lbl = QLabel(self.formLayoutWidget_2)
        self.segmentation_rawimg_lbl.setObjectName(u"segmentation_rawimg_lbl")
        self.segmentation_rawimg_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.segmentation_rawimg_lbl)

        self.segmentation_rawimg_chbox = QCheckBox(self.formLayoutWidget_2)
        self.segmentation_rawimg_chbox.setObjectName(u"segmentation_rawimg_chbox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.segmentation_rawimg_chbox)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_22)


        self.verticalLayout_7.addWidget(self.segmentation_down_Frame)

        self.stackedWidget.addWidget(self.segmentation_page)
        self.tarin_page = QWidget()
        self.tarin_page.setObjectName(u"tarin_page")
        self.verticalLayout_2 = QVBoxLayout(self.tarin_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.train_frame = QFrame(self.tarin_page)
        self.train_frame.setObjectName(u"train_frame")
        self.train_frame.setFrameShape(QFrame.StyledPanel)
        self.train_frame.setFrameShadow(QFrame.Raised)
        self.train_buttons_frame = QFrame(self.train_frame)
        self.train_buttons_frame.setObjectName(u"train_buttons_frame")
        self.train_buttons_frame.setGeometry(QRect(-1, 529, 1171, 171))
        self.train_buttons_frame.setStyleSheet(u"\n"
"background-color: rgb(89, 89, 89);")
        self.train_progbar = QProgressBar(self.train_buttons_frame)
        self.train_progbar.setObjectName(u"train_progbar")
        self.train_progbar.setGeometry(QRect(210, 110, 761, 20))
        sizePolicy3.setHeightForWidth(self.train_progbar.sizePolicy().hasHeightForWidth())
        self.train_progbar.setSizePolicy(sizePolicy3)
        self.train_progbar.setMinimumSize(QSize(20, 20))
        self.train_progbar.setFont(font1)
        self.train_progbar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-width: 2px;\n"
"	border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 14px;\n"
"	color: white;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #CD96CD;\n"
"	border-radius: 10px\n"
"}")
        self.train_progbar.setValue(0)
        self.train_progbar.setAlignment(Qt.AlignCenter)
        self.train_progbar.setTextVisible(True)
        self.horizontalLayoutWidget_2 = QWidget(self.train_buttons_frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 20, 1121, 41))
        self.train_main_buttons_layout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.train_main_buttons_layout.setObjectName(u"train_main_buttons_layout")
        self.train_main_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.train_main_buttons_layout.addItem(self.horizontalSpacer_9)

        self.train_browse_image_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.train_browse_image_btn.setObjectName(u"train_browse_image_btn")
        sizePolicy.setHeightForWidth(self.train_browse_image_btn.sizePolicy().hasHeightForWidth())
        self.train_browse_image_btn.setSizePolicy(sizePolicy)
        self.train_browse_image_btn.setMinimumSize(QSize(0, 31))
        self.train_browse_image_btn.setMaximumSize(QSize(10000, 10000))
        self.train_browse_image_btn.setStyleSheet(u"QPushButton {\n"
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
        self.train_browse_image_btn.setIcon(icon1)
        self.train_browse_image_btn.setIconSize(QSize(24, 24))

        self.train_main_buttons_layout.addWidget(self.train_browse_image_btn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.train_main_buttons_layout.addItem(self.horizontalSpacer_7)

        self.train_browse_masks_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.train_browse_masks_btn.setObjectName(u"train_browse_masks_btn")
        sizePolicy.setHeightForWidth(self.train_browse_masks_btn.sizePolicy().hasHeightForWidth())
        self.train_browse_masks_btn.setSizePolicy(sizePolicy)
        self.train_browse_masks_btn.setMinimumSize(QSize(0, 31))
        self.train_browse_masks_btn.setMaximumSize(QSize(10000, 10000))
        self.train_browse_masks_btn.setStyleSheet(u"QPushButton {\n"
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
        self.train_browse_masks_btn.setIcon(icon1)
        self.train_browse_masks_btn.setIconSize(QSize(24, 24))

        self.train_main_buttons_layout.addWidget(self.train_browse_masks_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.train_main_buttons_layout.addItem(self.horizontalSpacer_5)

        self.train_start_training_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.train_start_training_btn.setObjectName(u"train_start_training_btn")
        sizePolicy.setHeightForWidth(self.train_start_training_btn.sizePolicy().hasHeightForWidth())
        self.train_start_training_btn.setSizePolicy(sizePolicy)
        self.train_start_training_btn.setMinimumSize(QSize(0, 31))
        self.train_start_training_btn.setMaximumSize(QSize(10000, 10000))
        self.train_start_training_btn.setStyleSheet(u"QPushButton {\n"
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
        self.train_start_training_btn.setIcon(icon2)
        self.train_start_training_btn.setIconSize(QSize(24, 24))

        self.train_main_buttons_layout.addWidget(self.train_start_training_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.train_main_buttons_layout.addItem(self.horizontalSpacer_6)

        self.train_stop_training_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.train_stop_training_btn.setObjectName(u"train_stop_training_btn")
        sizePolicy.setHeightForWidth(self.train_stop_training_btn.sizePolicy().hasHeightForWidth())
        self.train_stop_training_btn.setSizePolicy(sizePolicy)
        self.train_stop_training_btn.setMinimumSize(QSize(0, 31))
        self.train_stop_training_btn.setMaximumSize(QSize(10000, 10000))
        self.train_stop_training_btn.setStyleSheet(u"QPushButton {\n"
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
        self.train_stop_training_btn.setIcon(icon3)
        self.train_stop_training_btn.setIconSize(QSize(24, 24))

        self.train_main_buttons_layout.addWidget(self.train_stop_training_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.train_main_buttons_layout.addItem(self.horizontalSpacer_8)

        self.train_prog_lbl = QLabel(self.train_buttons_frame)
        self.train_prog_lbl.setObjectName(u"train_prog_lbl")
        self.train_prog_lbl.setGeometry(QRect(375, 140, 431, 20))
        self.train_prog_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";")
        self.train_prog_lbl.setAlignment(Qt.AlignCenter)
        self.train_image_lstwdg = QListWidget(self.train_frame)
        self.train_image_lstwdg.setObjectName(u"train_image_lstwdg")
        self.train_image_lstwdg.setGeometry(QRect(20, 30, 341, 221))
        self.train_image_lstwdg.setStyleSheet(u"background-color: rgb(88, 88, 88);")
        self.train_rights_lbl = QLabel(self.train_frame)
        self.train_rights_lbl.setObjectName(u"train_rights_lbl")
        self.train_rights_lbl.setGeometry(QRect(369, 703, 441, 21))
        self.train_rights_lbl.setFont(font4)
        self.train_rights_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_2 = QWidget(self.train_frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(100, 260, 190, 168))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.train_image_selectall_btn = QPushButton(self.verticalLayoutWidget_2)
        self.train_image_selectall_btn.setObjectName(u"train_image_selectall_btn")
        sizePolicy.setHeightForWidth(self.train_image_selectall_btn.sizePolicy().hasHeightForWidth())
        self.train_image_selectall_btn.setSizePolicy(sizePolicy)
        self.train_image_selectall_btn.setMinimumSize(QSize(0, 31))
        self.train_image_selectall_btn.setMaximumSize(QSize(10000, 10000))
        self.train_image_selectall_btn.setFont(font1)
        self.train_image_selectall_btn.setAutoFillBackground(False)
        self.train_image_selectall_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_image_selectall_btn.setIcon(icon7)
        self.train_image_selectall_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.train_image_selectall_btn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.train_image_unselectall_btn = QPushButton(self.verticalLayoutWidget_2)
        self.train_image_unselectall_btn.setObjectName(u"train_image_unselectall_btn")
        sizePolicy.setHeightForWidth(self.train_image_unselectall_btn.sizePolicy().hasHeightForWidth())
        self.train_image_unselectall_btn.setSizePolicy(sizePolicy)
        self.train_image_unselectall_btn.setMinimumSize(QSize(0, 31))
        self.train_image_unselectall_btn.setMaximumSize(QSize(10000, 10000))
        self.train_image_unselectall_btn.setFont(font1)
        self.train_image_unselectall_btn.setAutoFillBackground(False)
        self.train_image_unselectall_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_image_unselectall_btn.setIcon(icon8)
        self.train_image_unselectall_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.train_image_unselectall_btn)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.train_clear_unselect_images_btn = QPushButton(self.verticalLayoutWidget_2)
        self.train_clear_unselect_images_btn.setObjectName(u"train_clear_unselect_images_btn")
        sizePolicy.setHeightForWidth(self.train_clear_unselect_images_btn.sizePolicy().hasHeightForWidth())
        self.train_clear_unselect_images_btn.setSizePolicy(sizePolicy)
        self.train_clear_unselect_images_btn.setMinimumSize(QSize(0, 31))
        self.train_clear_unselect_images_btn.setMaximumSize(QSize(10000, 10000))
        self.train_clear_unselect_images_btn.setFont(font1)
        self.train_clear_unselect_images_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_clear_unselect_images_btn.setIcon(icon8)
        self.train_clear_unselect_images_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.train_clear_unselect_images_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.train_clearimages_btn = QPushButton(self.verticalLayoutWidget_2)
        self.train_clearimages_btn.setObjectName(u"train_clearimages_btn")
        sizePolicy.setHeightForWidth(self.train_clearimages_btn.sizePolicy().hasHeightForWidth())
        self.train_clearimages_btn.setSizePolicy(sizePolicy)
        self.train_clearimages_btn.setMinimumSize(QSize(0, 31))
        self.train_clearimages_btn.setMaximumSize(QSize(10000, 10000))
        self.train_clearimages_btn.setFont(font1)
        self.train_clearimages_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_clearimages_btn.setIcon(icon9)
        self.train_clearimages_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.train_clearimages_btn)

        self.gridLayoutWidget_2 = QWidget(self.train_frame)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(80, 440, 227, 62))
        self.train_selected_layout = QGridLayout(self.gridLayoutWidget_2)
        self.train_selected_layout.setObjectName(u"train_selected_layout")
        self.train_selected_layout.setContentsMargins(0, 0, 0, 0)
        self.train_unselected_images_lcd = QLCDNumber(self.gridLayoutWidget_2)
        self.train_unselected_images_lcd.setObjectName(u"train_unselected_images_lcd")

        self.train_selected_layout.addWidget(self.train_unselected_images_lcd, 2, 1, 1, 1)

        self.train_selected_images_lbl = QLabel(self.gridLayoutWidget_2)
        self.train_selected_images_lbl.setObjectName(u"train_selected_images_lbl")
        self.train_selected_images_lbl.setFont(font5)
        self.train_selected_images_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.train_selected_layout.addWidget(self.train_selected_images_lbl, 0, 0, 1, 1)

        self.train_unselected_images_lbl = QLabel(self.gridLayoutWidget_2)
        self.train_unselected_images_lbl.setObjectName(u"train_unselected_images_lbl")
        self.train_unselected_images_lbl.setFont(font5)
        self.train_unselected_images_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.train_selected_layout.addWidget(self.train_unselected_images_lbl, 2, 0, 1, 1)

        self.train_selected_images_lcd = QLCDNumber(self.gridLayoutWidget_2)
        self.train_selected_images_lcd.setObjectName(u"train_selected_images_lcd")

        self.train_selected_layout.addWidget(self.train_selected_images_lcd, 0, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_selected_layout.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_selected_layout.addItem(self.verticalSpacer_10, 1, 1, 1, 1)

        self.formLayoutWidget = QWidget(self.train_frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(420, 50, 310, 181))
        self.train_pram_layout = QFormLayout(self.formLayoutWidget)
        self.train_pram_layout.setObjectName(u"train_pram_layout")
        self.train_pram_layout.setLabelAlignment(Qt.AlignCenter)
        self.train_pram_layout.setFormAlignment(Qt.AlignCenter)
        self.train_pram_layout.setContentsMargins(0, 0, 0, 0)
        self.train_modelname_lbl = QLabel(self.formLayoutWidget)
        self.train_modelname_lbl.setObjectName(u"train_modelname_lbl")
        self.train_modelname_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";")

        self.train_pram_layout.setWidget(0, QFormLayout.LabelRole, self.train_modelname_lbl)

        self.train_model_name_txtbox = QLineEdit(self.formLayoutWidget)
        self.train_model_name_txtbox.setObjectName(u"train_model_name_txtbox")
        self.train_model_name_txtbox.setLayoutDirection(Qt.LeftToRight)
        self.train_model_name_txtbox.setStyleSheet(u"border-style: outset;\n"
"border-width: 3px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";\n"
"border-radius: 10px;\n"
"border-color: rgb(66, 66, 66);")
        self.train_model_name_txtbox.setText(u"")
        self.train_model_name_txtbox.setAlignment(Qt.AlignCenter)

        self.train_pram_layout.setWidget(0, QFormLayout.FieldRole, self.train_model_name_txtbox)

        self.tain_epochs_lbl = QLabel(self.formLayoutWidget)
        self.tain_epochs_lbl.setObjectName(u"tain_epochs_lbl")
        self.tain_epochs_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";")

        self.train_pram_layout.setWidget(2, QFormLayout.LabelRole, self.tain_epochs_lbl)

        self.train_batchsize_lbl = QLabel(self.formLayoutWidget)
        self.train_batchsize_lbl.setObjectName(u"train_batchsize_lbl")
        self.train_batchsize_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";")

        self.train_pram_layout.setWidget(4, QFormLayout.LabelRole, self.train_batchsize_lbl)

        self.train_epoch_number_txtbox = QLineEdit(self.formLayoutWidget)
        self.train_epoch_number_txtbox.setObjectName(u"train_epoch_number_txtbox")
        self.train_epoch_number_txtbox.setLayoutDirection(Qt.LeftToRight)
        self.train_epoch_number_txtbox.setStyleSheet(u"border-style: outset;\n"
"border-width: 3px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";\n"
"border-radius: 10px;\n"
"border-color: rgb(66, 66, 66);")
        self.train_epoch_number_txtbox.setText(u"")
        self.train_epoch_number_txtbox.setAlignment(Qt.AlignCenter)

        self.train_pram_layout.setWidget(2, QFormLayout.FieldRole, self.train_epoch_number_txtbox)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_pram_layout.setItem(1, QFormLayout.FieldRole, self.verticalSpacer_11)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_pram_layout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_12)

        self.train_imagesize_lbl = QLabel(self.formLayoutWidget)
        self.train_imagesize_lbl.setObjectName(u"train_imagesize_lbl")
        self.train_imagesize_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Aharoni\";")

        self.train_pram_layout.setWidget(6, QFormLayout.LabelRole, self.train_imagesize_lbl)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_pram_layout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_13)

        self.train_batchsize_combox = QComboBox(self.formLayoutWidget)
        self.train_batchsize_combox.addItem("")
        self.train_batchsize_combox.addItem("")
        self.train_batchsize_combox.addItem("")
        self.train_batchsize_combox.addItem("")
        self.train_batchsize_combox.addItem("")
        self.train_batchsize_combox.addItem("")
        self.train_batchsize_combox.setObjectName(u"train_batchsize_combox")
        self.train_batchsize_combox.setStyleSheet(u"border-style: outset;\n"
"border-width: 3px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Aharoni\";\n"
"border-radius: 10px;\n"
"border-color: rgb(66, 66, 66);\n"
"padding-left: 70px;")

        self.train_pram_layout.setWidget(4, QFormLayout.FieldRole, self.train_batchsize_combox)

        self.train_imagesize_combox = QComboBox(self.formLayoutWidget)
        self.train_imagesize_combox.addItem("")
        self.train_imagesize_combox.addItem("")
        self.train_imagesize_combox.setObjectName(u"train_imagesize_combox")
        self.train_imagesize_combox.setStyleSheet(u"border-style: outset;\n"
"border-width: 3px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Aharoni\";\n"
"border-radius: 10px;\n"
"border-color: rgb(66, 66, 66);\n"
"padding-left: 70px;")

        self.train_pram_layout.setWidget(6, QFormLayout.FieldRole, self.train_imagesize_combox)

        self.train_mask_lstwdg = QListWidget(self.train_frame)
        self.train_mask_lstwdg.setObjectName(u"train_mask_lstwdg")
        self.train_mask_lstwdg.setGeometry(QRect(800, 30, 341, 221))
        self.train_mask_lstwdg.setStyleSheet(u"background-color: rgb(88, 88, 88);")
        self.gridLayoutWidget_3 = QWidget(self.train_frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(870, 440, 227, 62))
        self.train_selected_layout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.train_selected_layout_2.setObjectName(u"train_selected_layout_2")
        self.train_selected_layout_2.setContentsMargins(0, 0, 0, 0)
        self.train_unselected_masks_lcd = QLCDNumber(self.gridLayoutWidget_3)
        self.train_unselected_masks_lcd.setObjectName(u"train_unselected_masks_lcd")

        self.train_selected_layout_2.addWidget(self.train_unselected_masks_lcd, 2, 1, 1, 1)

        self.train_selected_images_lbl_2 = QLabel(self.gridLayoutWidget_3)
        self.train_selected_images_lbl_2.setObjectName(u"train_selected_images_lbl_2")
        self.train_selected_images_lbl_2.setFont(font5)
        self.train_selected_images_lbl_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.train_selected_layout_2.addWidget(self.train_selected_images_lbl_2, 0, 0, 1, 1)

        self.train_unselected_images_lbl_2 = QLabel(self.gridLayoutWidget_3)
        self.train_unselected_images_lbl_2.setObjectName(u"train_unselected_images_lbl_2")
        self.train_unselected_images_lbl_2.setFont(font5)
        self.train_unselected_images_lbl_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.train_selected_layout_2.addWidget(self.train_unselected_images_lbl_2, 2, 0, 1, 1)

        self.train_selected_masks_lcd = QLCDNumber(self.gridLayoutWidget_3)
        self.train_selected_masks_lcd.setObjectName(u"train_selected_masks_lcd")

        self.train_selected_layout_2.addWidget(self.train_selected_masks_lcd, 0, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_selected_layout_2.addItem(self.verticalSpacer_16, 1, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_selected_layout_2.addItem(self.verticalSpacer_17, 1, 1, 1, 1)

        self.verticalLayoutWidget_3 = QWidget(self.train_frame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(890, 260, 190, 168))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.train_selectall_masks_btn = QPushButton(self.verticalLayoutWidget_3)
        self.train_selectall_masks_btn.setObjectName(u"train_selectall_masks_btn")
        sizePolicy.setHeightForWidth(self.train_selectall_masks_btn.sizePolicy().hasHeightForWidth())
        self.train_selectall_masks_btn.setSizePolicy(sizePolicy)
        self.train_selectall_masks_btn.setMinimumSize(QSize(0, 31))
        self.train_selectall_masks_btn.setMaximumSize(QSize(10000, 10000))
        self.train_selectall_masks_btn.setFont(font1)
        self.train_selectall_masks_btn.setAutoFillBackground(False)
        self.train_selectall_masks_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_selectall_masks_btn.setIcon(icon7)
        self.train_selectall_masks_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.train_selectall_masks_btn)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_18)

        self.train_unselectall_masks_btn = QPushButton(self.verticalLayoutWidget_3)
        self.train_unselectall_masks_btn.setObjectName(u"train_unselectall_masks_btn")
        sizePolicy.setHeightForWidth(self.train_unselectall_masks_btn.sizePolicy().hasHeightForWidth())
        self.train_unselectall_masks_btn.setSizePolicy(sizePolicy)
        self.train_unselectall_masks_btn.setMinimumSize(QSize(0, 31))
        self.train_unselectall_masks_btn.setMaximumSize(QSize(10000, 10000))
        self.train_unselectall_masks_btn.setFont(font1)
        self.train_unselectall_masks_btn.setAutoFillBackground(False)
        self.train_unselectall_masks_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_unselectall_masks_btn.setIcon(icon8)
        self.train_unselectall_masks_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.train_unselectall_masks_btn)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_19)

        self.train_clear_unselect_masks_btn = QPushButton(self.verticalLayoutWidget_3)
        self.train_clear_unselect_masks_btn.setObjectName(u"train_clear_unselect_masks_btn")
        sizePolicy.setHeightForWidth(self.train_clear_unselect_masks_btn.sizePolicy().hasHeightForWidth())
        self.train_clear_unselect_masks_btn.setSizePolicy(sizePolicy)
        self.train_clear_unselect_masks_btn.setMinimumSize(QSize(0, 31))
        self.train_clear_unselect_masks_btn.setMaximumSize(QSize(10000, 10000))
        self.train_clear_unselect_masks_btn.setFont(font1)
        self.train_clear_unselect_masks_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_clear_unselect_masks_btn.setIcon(icon8)
        self.train_clear_unselect_masks_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.train_clear_unselect_masks_btn)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_20)

        self.train_cleamasks_btn = QPushButton(self.verticalLayoutWidget_3)
        self.train_cleamasks_btn.setObjectName(u"train_cleamasks_btn")
        sizePolicy.setHeightForWidth(self.train_cleamasks_btn.sizePolicy().hasHeightForWidth())
        self.train_cleamasks_btn.setSizePolicy(sizePolicy)
        self.train_cleamasks_btn.setMinimumSize(QSize(0, 31))
        self.train_cleamasks_btn.setMaximumSize(QSize(10000, 10000))
        self.train_cleamasks_btn.setFont(font1)
        self.train_cleamasks_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(66, 66, 66);\n"
"    font: bold 11px;\n"
"    padding: 6px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.train_cleamasks_btn.setIcon(icon9)
        self.train_cleamasks_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.train_cleamasks_btn)


        self.verticalLayout_2.addWidget(self.train_frame)

        self.stackedWidget.addWidget(self.tarin_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.verticalLayout_8 = QVBoxLayout(self.help_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.help_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 30, 121, 31))
        font7 = QFont()
        font7.setFamily(u"Aharoni")
        font7.setPointSize(16)
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(310, 180, 471, 301))
        self.frame_4.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 451, 191))
        font8 = QFont()
        font8.setFamily(u"Aharoni")
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.label.setFont(font8)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.rights_lbl_3 = QLabel(self.frame_3)
        self.rights_lbl_3.setObjectName(u"rights_lbl_3")
        self.rights_lbl_3.setGeometry(QRect(350, 700, 431, 21))
        self.rights_lbl_3.setFont(font4)
        self.rights_lbl_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.help_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.horizontalLayout_3 = QHBoxLayout(self.about_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.about_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(360, 210, 411, 301))
        self.frame_2.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_4 = QWidget(self.frame_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 60, 381, 171))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")
        font9 = QFont()
        font9.setFamily(u"Aharoni")
        font9.setPointSize(14)
        font9.setKerning(True)
        self.label_3.setFont(font9)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3)

        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font9)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_21)

        self.label_4 = QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font9)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.label_6 = QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font9)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 531, 31))
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rights_lbl_2 = QLabel(self.frame)
        self.rights_lbl_2.setObjectName(u"rights_lbl_2")
        self.rights_lbl_2.setGeometry(QRect(380, 710, 431, 21))
        self.rights_lbl_2.setFont(font4)
        self.rights_lbl_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.frame)

        self.stackedWidget.addWidget(self.about_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Microdroplets Identification & Segmentation", None))
        self.Btn_Toggle.setText("")
        self.segmentation_page_btn.setText(QCoreApplication.translate("MainWindow", u"Sementation", None))
        self.training_page_btn.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.help_page_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.about_page_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.segmentation_browse_btn.setText(QCoreApplication.translate("MainWindow", u"  Insert Image", None))
        self.segmentation_start_segmentation_btn.setText(QCoreApplication.translate("MainWindow", u" Start Segmentation", None))
        self.segmentation_stop_segmentation_btn.setText(QCoreApplication.translate("MainWindow", u" Stop Segmentation", None))
        self.segmentation_show_results_btn.setText(QCoreApplication.translate("MainWindow", u" Show Results", None))
        self.segmentation_downloadresults_btn.setText(QCoreApplication.translate("MainWindow", u" Download Results", None))
        self.segmentation_reset_btn.setText(QCoreApplication.translate("MainWindow", u" Reset", None))
        self.segmentation_info_progbar_lbl.setText("")
        self.segmentation_image_lbl.setText(QCoreApplication.translate("MainWindow", u"Please insert image to view on the screen", None))
        self.rights_lbl.setText(QCoreApplication.translate("MainWindow", u"Developed By Loai Ab & Moataz Ata  \u00a9\ufe0f 2021 All rights reserved", None))
        self.segmentation_selected_images_lbl.setText(QCoreApplication.translate("MainWindow", u"SELECTED IMAGES", None))
        self.segmentation_unselected_images_lbl.setText(QCoreApplication.translate("MainWindow", u"UNSELECTED IMAGES", None))
        self.segmentation_selectall_btn.setText(QCoreApplication.translate("MainWindow", u"  Select All", None))
        self.segmentation_unselectall_btn.setText(QCoreApplication.translate("MainWindow", u"  Unselect All", None))
        self.segmentation_clear_unselect_images_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Unselected Images", None))
        self.segmentation_clearimages_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Images", None))
        self.segmentation_imagesize_lbl.setText(QCoreApplication.translate("MainWindow", u"Image Batch Size :", None))
        self.segmentation_batchsize_256_radbtn.setText(QCoreApplication.translate("MainWindow", u"256", None))
        self.segmentation_batchsize_512_radbtn.setText(QCoreApplication.translate("MainWindow", u"512", None))
        self.segmentation_rawimg_lbl.setText(QCoreApplication.translate("MainWindow", u"Raw Image :", None))
        self.segmentation_rawimg_chbox.setText("")
        self.train_progbar.setFormat("")
        self.train_browse_image_btn.setText(QCoreApplication.translate("MainWindow", u"  Insert Image", None))
        self.train_browse_masks_btn.setText(QCoreApplication.translate("MainWindow", u"  Insert Mask", None))
        self.train_start_training_btn.setText(QCoreApplication.translate("MainWindow", u" Start Training", None))
        self.train_stop_training_btn.setText(QCoreApplication.translate("MainWindow", u" Stop Training", None))
        self.train_prog_lbl.setText("")
        self.train_rights_lbl.setText(QCoreApplication.translate("MainWindow", u"Developed By Loai Ab & Moataz Ata  \u00a9\ufe0f 2021 All rights reserved", None))
        self.train_image_selectall_btn.setText(QCoreApplication.translate("MainWindow", u"  Select All", None))
        self.train_image_unselectall_btn.setText(QCoreApplication.translate("MainWindow", u"  Unselect All", None))
        self.train_clear_unselect_images_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Unselected Images", None))
        self.train_clearimages_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Images", None))
        self.train_selected_images_lbl.setText(QCoreApplication.translate("MainWindow", u"SELECTED IMAGES", None))
        self.train_unselected_images_lbl.setText(QCoreApplication.translate("MainWindow", u"UNSELECTED IMAGES", None))
        self.train_modelname_lbl.setText(QCoreApplication.translate("MainWindow", u"Model Name :", None))
        self.tain_epochs_lbl.setText(QCoreApplication.translate("MainWindow", u"Number Of Epochs :", None))
        self.train_batchsize_lbl.setText(QCoreApplication.translate("MainWindow", u"Batch Size :", None))
        self.train_imagesize_lbl.setText(QCoreApplication.translate("MainWindow", u"Image Batch Size :", None))
        self.train_batchsize_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.train_batchsize_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"8", None))
        self.train_batchsize_combox.setItemText(2, QCoreApplication.translate("MainWindow", u"12", None))
        self.train_batchsize_combox.setItemText(3, QCoreApplication.translate("MainWindow", u"16", None))
        self.train_batchsize_combox.setItemText(4, QCoreApplication.translate("MainWindow", u"24", None))
        self.train_batchsize_combox.setItemText(5, QCoreApplication.translate("MainWindow", u"32", None))

        self.train_imagesize_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"256", None))
        self.train_imagesize_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"512", None))

        self.train_selected_images_lbl_2.setText(QCoreApplication.translate("MainWindow", u"SELECTED MASKS", None))
        self.train_unselected_images_lbl_2.setText(QCoreApplication.translate("MainWindow", u"UNSELECTED MASKS", None))
        self.train_selectall_masks_btn.setText(QCoreApplication.translate("MainWindow", u"  Select All", None))
        self.train_unselectall_masks_btn.setText(QCoreApplication.translate("MainWindow", u"  Unselect All", None))
        self.train_clear_unselect_masks_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Unselected Images", None))
        self.train_cleamasks_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Images", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Help:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"For Any Operating Instructions \n"
"\n"
" Please review the instructions PDF file \n"
"\n"
" in the Google drive", None))
        self.rights_lbl_3.setText(QCoreApplication.translate("MainWindow", u"Developed By Loai Ab & Moataz Ata  \u00a9\ufe0f 2021 All rights reserved", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Loai Abedalhi", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email: loaiabwork@gmail.com", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Moataz Atawna", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email: mtzatawna@gmail.com", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Developers Contact Information:", None))
        self.rights_lbl_2.setText(QCoreApplication.translate("MainWindow", u"Developed By Loai Ab & Moataz Ata  \u00a9\ufe0f 2021 All rights reserved", None))
    # retranslateUi

