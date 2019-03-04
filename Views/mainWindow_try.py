# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/resources/qt files/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Views import guiResource
from enum import Enum


class MainWindow(object):
    # Page = Enum('WELCOME', 'TRAIN_GUIDE', 'TEST_GUIDE', 'TEST_GUIDE')
    class Page(Enum):
        WELCOME = 0
        TRAIN_GUIDE = 1
        TEST_GUIDE = 2
        TRAIN_LEARNER = 3
        TEST_LEARNER = 4
        ABOUT = 5
        HOW_TO_USE = 6

    def setupUi(self, MainWindow, controller):
        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(526, 517)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet("QStatusBar#statusBar\n"
                                 "{\n"
                                 "    /*border-image: url(:/Background/background.jpg);*/\n"
                                 "}")
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setStyleSheet("QWidget#centralWidget\n"
                                         "{\n"
                                         "    border-image: url(:/Background/background.jpg);\n"
                                         "}")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setContentsMargins(-1, 20, -1, -1)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName("mainLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Welcome = QtWidgets.QWidget()
        self.Welcome.setObjectName("Welcome")
        self.gridLayout = QtWidgets.QGridLayout(self.Welcome)
        self.gridLayout.setObjectName("gridLayout")
        self.welcomLayout = QtWidgets.QGridLayout()
        self.welcomLayout.setSpacing(0)
        self.welcomLayout.setObjectName("welcomLayout")
        self.faceRecTitle = QtWidgets.QLabel(self.Welcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faceRecTitle.sizePolicy().hasHeightForWidth())
        self.faceRecTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        self.faceRecTitle.setFont(font)
        self.faceRecTitle.setStyleSheet("")
        self.faceRecTitle.setObjectName("faceRecTitle")
        self.welcomLayout.addWidget(self.faceRecTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.faceRecImage = QtWidgets.QLabel(self.Welcome)
        self.faceRecImage.setObjectName("faceRecImage")
        self.welcomLayout.addWidget(self.faceRecImage, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.welcomLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Welcome)
        self.Training = QtWidgets.QWidget()
        self.Training.setObjectName("Training")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Training)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.trainingLayout = QtWidgets.QGridLayout()
        self.trainingLayout.setHorizontalSpacing(0)
        self.trainingLayout.setVerticalSpacing(20)
        self.trainingLayout.setObjectName("trainingLayout")
        self.browseBoxTraining = QtWidgets.QGroupBox(self.Training)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBoxTraining.sizePolicy().hasHeightForWidth())
        self.browseBoxTraining.setSizePolicy(sizePolicy)
        self.browseBoxTraining.setMinimumSize(QtCore.QSize(0, 60))
        self.browseBoxTraining.setStyleSheet("border-style: none")
        self.browseBoxTraining.setTitle("")
        self.browseBoxTraining.setFlat(False)
        self.browseBoxTraining.setCheckable(False)
        self.browseBoxTraining.setObjectName("browseBoxTraining")
        self.browseBtnTraining = QtWidgets.QPushButton(self.browseBoxTraining)
        self.browseBtnTraining.setGeometry(QtCore.QRect(319, 6, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnTraining.sizePolicy().hasHeightForWidth())
        self.browseBtnTraining.setSizePolicy(sizePolicy)
        self.browseBtnTraining.setStyleSheet("QPushButton#browseBtnTraining:hover\n"
                                             "{\n"
                                             "    image: url(:/BrowseBtn/browseHover.png);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#browseBtnTraining:pressed\n"
                                             "{\n"
                                             "    image: url(:/BrowseBtn/browsePush.png);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#browseBtnTraining\n"
                                             "{\n"
                                             "    image: url(:/BrowseBtn/browseDef.png);\n"
                                             "    background:transparent;\n"
                                             "\n"
                                             "}")
        self.browseBtnTraining.setText("")
        self.browseBtnTraining.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnTraining.setAutoRepeatDelay(4)
        self.browseBtnTraining.setAutoRepeatInterval(4)
        self.browseBtnTraining.setObjectName("browseBtnTraining")
        self.customizeTextboxTraining = QtWidgets.QLabel(self.browseBoxTraining)
        self.customizeTextboxTraining.setGeometry(QtCore.QRect(4, 10, 311, 41))
        self.customizeTextboxTraining.setObjectName("customizeTextboxTraining")
        self.trainingDir = QtWidgets.QLineEdit(self.browseBoxTraining)
        self.trainingDir.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trainingDir.setFont(font)
        self.trainingDir.setAutoFillBackground(False)
        self.trainingDir.setStyleSheet("QLineEdit \n"
                                       "{\n"
                                       "    background:transparent\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.trainingDir.setText("")
        self.trainingDir.setFrame(False)
        self.trainingDir.setObjectName("trainingDir")
        self.customizeTextboxTraining.raise_()
        self.trainingDir.raise_()
        self.browseBtnTraining.raise_()
        self.trainingLayout.addWidget(self.browseBoxTraining, 1, 0, 1, 1)
        self.title = QtWidgets.QLabel(self.Training)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.trainingLayout.addWidget(self.title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.trainingLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.trainBtn = QtWidgets.QPushButton(self.Training)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainBtn.sizePolicy().hasHeightForWidth())
        self.trainBtn.setSizePolicy(sizePolicy)
        self.trainBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.trainBtn.setStyleSheet("\n"
                                    "QPushButton#trainBtn:hover\n"
                                    "{\n"
                                    "    image: url(:/StartTrainingBtn/startTrainingHover.png);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#trainBtn:pressed\n"
                                    "{\n"
                                    "    image: url(:/StartTrainingBtn/startTrainingPush.png);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#trainBtn\n"
                                    "{\n"
                                    "    image: url(:/StartTrainingBtn/startTrainingDef.png);\n"
                                    "    background:transparent;\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "")
        self.trainBtn.setText("")
        self.trainBtn.setIconSize(QtCore.QSize(10, 10))
        self.trainBtn.setAutoRepeatDelay(4)
        self.trainBtn.setAutoRepeatInterval(4)
        self.trainBtn.setObjectName("trainBtn")
        self.trainingLayout.addWidget(self.trainBtn, 3, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.trainingLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Training)
        self.Testing = QtWidgets.QWidget()
        self.Testing.setObjectName("Testing")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Testing)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TestingLayout = QtWidgets.QGridLayout()
        self.TestingLayout.setSpacing(0)
        self.TestingLayout.setObjectName("TestingLayout")
        # self.testingTitle = QtWidgets.QLabel(self.Testing)
        self.title.setParent(self.Testing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.testingTitle.sizePolicy().hasHeightForWidth())
        # self.testingTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        # self.testingTitle.setFont(font)
        # self.testingTitle.setObjectName("testingTitle")
        # self.TestingLayout.addWidget(self.testingTitle, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.ImageDirLayout2 = QtWidgets.QHBoxLayout()
        self.ImageDirLayout2.setContentsMargins(20, 0, -1, 0)
        self.ImageDirLayout2.setSpacing(0)
        self.ImageDirLayout2.setObjectName("ImageDirLayout2")
        self.chosenImg = QtWidgets.QLabel(self.Testing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chosenImg.sizePolicy().hasHeightForWidth())
        self.chosenImg.setSizePolicy(sizePolicy)
        self.chosenImg.setMinimumSize(QtCore.QSize(210, 210))
        self.chosenImg.setStyleSheet("QLabel#chosenImg\n"
                                     "{\n"
                                     "border-image: url(:/DefaultImage/defualtImage.png);\n"
                                     "\n"
                                     "}")
        self.chosenImg.setText("")
        self.chosenImg.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.chosenImg.setObjectName("chosenImg")
        self.ImageDirLayout2.addWidget(self.chosenImg)
        self.testBtn = QtWidgets.QPushButton(self.Testing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testBtn.sizePolicy().hasHeightForWidth())
        self.testBtn.setSizePolicy(sizePolicy)
        self.testBtn.setMinimumSize(QtCore.QSize(85, 40))
        self.testBtn.setStyleSheet("\n"
                                   "QPushButton#testBtn:hover\n"
                                   "{\n"
                                   "    \n"
                                   "    image: url(:/TestBtn/testHover.png);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#testBtn:pressed\n"
                                   "{\n"
                                   "    \n"
                                   "    image: url(:/TestBtn/testPush.png);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#testBtn\n"
                                   "{\n"
                                   "    \n"
                                   "    image: url(:/TestBtn/testDef.png);\n"
                                   "    background:transparent;\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "")
        self.testBtn.setText("")
        self.testBtn.setIconSize(QtCore.QSize(10, 10))
        self.testBtn.setAutoRepeatDelay(4)
        self.testBtn.setAutoRepeatInterval(4)
        self.testBtn.setObjectName("testBtn")
        self.ImageDirLayout2.addWidget(self.testBtn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.TestingLayout.addLayout(self.ImageDirLayout2, 4, 0, 1, 2)
        self.ImageDirLayout = QtWidgets.QVBoxLayout()
        self.ImageDirLayout.setContentsMargins(-1, 20, -1, -1)
        self.ImageDirLayout.setObjectName("ImageDirLayout")
        self.browseBoxTesting_2 = QtWidgets.QGroupBox(self.Testing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBoxTesting_2.sizePolicy().hasHeightForWidth())
        self.browseBoxTesting_2.setSizePolicy(sizePolicy)
        self.browseBoxTesting_2.setMinimumSize(QtCore.QSize(0, 60))
        self.browseBoxTesting_2.setStyleSheet("border-style: none")
        self.browseBoxTesting_2.setTitle("")
        self.browseBoxTesting_2.setFlat(False)
        self.browseBoxTesting_2.setCheckable(False)
        self.browseBoxTesting_2.setObjectName("browseBoxTesting_2")
        self.browseBtnModel = QtWidgets.QPushButton(self.browseBoxTesting_2)
        self.browseBtnModel.setGeometry(QtCore.QRect(319, 6, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnModel.sizePolicy().hasHeightForWidth())
        self.browseBtnModel.setSizePolicy(sizePolicy)
        self.browseBtnModel.setStyleSheet("QPushButton#browseBtnModel:hover\n"
                                          "{\n"
                                          "    image: url(:/BrowseBtn/browseHover.png);\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#browseBtnModel:pressed\n"
                                          "{\n"
                                          "    image: url(:/BrowseBtn/browsePush.png);\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#browseBtnModel\n"
                                          "{\n"
                                          "    image: url(:/BrowseBtn/browseDef.png);\n"
                                          "    background:transparent;\n"
                                          "\n"
                                          "}")
        self.browseBtnModel.setText("")
        self.browseBtnModel.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnModel.setAutoRepeatDelay(4)
        self.browseBtnModel.setAutoRepeatInterval(4)
        self.browseBtnModel.setObjectName("browseBtnModel")
        self.customizeTextboxModelTesting = QtWidgets.QLabel(self.browseBoxTesting_2)
        self.customizeTextboxModelTesting.setGeometry(QtCore.QRect(4, 10, 311, 41))
        self.customizeTextboxModelTesting.setObjectName("customizeTextboxModelTesting")
        self.modelDir = QtWidgets.QLineEdit(self.browseBoxTesting_2)
        self.modelDir.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.modelDir.setFont(font)
        self.modelDir.setAutoFillBackground(False)
        self.modelDir.setStyleSheet("QLineEdit \n"
                                    "{\n"
                                    "    background:transparent\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.modelDir.setText("")
        self.modelDir.setFrame(False)
        self.modelDir.setObjectName("modelDir")
        self.ImageDirLayout.addWidget(self.browseBoxTesting_2)
        self.browseBoxTesting_1 = QtWidgets.QGroupBox(self.Testing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBoxTesting_1.sizePolicy().hasHeightForWidth())
        self.browseBoxTesting_1.setSizePolicy(sizePolicy)
        self.browseBoxTesting_1.setMinimumSize(QtCore.QSize(440, 60))
        self.browseBoxTesting_1.setStyleSheet("border-style: none;\n"
                                              "")
        self.browseBoxTesting_1.setTitle("")
        self.browseBoxTesting_1.setFlat(False)
        self.browseBoxTesting_1.setCheckable(False)
        self.browseBoxTesting_1.setObjectName("browseBoxTesting_1")
        self.browseBtnImgTesting = QtWidgets.QPushButton(self.browseBoxTesting_1)
        self.browseBtnImgTesting.setGeometry(QtCore.QRect(319, 6, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnImgTesting.sizePolicy().hasHeightForWidth())
        self.browseBtnImgTesting.setSizePolicy(sizePolicy)
        self.browseBtnImgTesting.setStyleSheet("QPushButton#browseBtnImgTesting:hover\n"
                                               "{\n"
                                               "    image: url(:/BrowseBtn/browseHover.png);\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#browseBtnImgTesting:pressed\n"
                                               "{\n"
                                               "    image: url(:/BrowseBtn/browsePush.png);\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#browseBtnImgTesting\n"
                                               "{\n"
                                               "    image: url(:/BrowseBtn/browseDef.png);\n"
                                               "    background:transparent;\n"
                                               "\n"
                                               "}")
        self.browseBtnImgTesting.setText("")
        self.browseBtnImgTesting.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnImgTesting.setAutoRepeatDelay(4)
        self.browseBtnImgTesting.setAutoRepeatInterval(4)
        self.browseBtnImgTesting.setObjectName("browseBtnImgTesting")
        self.customizeTextboxImgTesting = QtWidgets.QLabel(self.browseBoxTesting_1)
        self.customizeTextboxImgTesting.setGeometry(QtCore.QRect(4, 10, 311, 41))
        self.customizeTextboxImgTesting.setObjectName("customizeTextboxImgTesting")
        self.imgDir = QtWidgets.QLineEdit(self.browseBoxTesting_1)
        self.imgDir.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.imgDir.setFont(font)
        self.imgDir.setAutoFillBackground(False)
        self.imgDir.setStyleSheet("QLineEdit \n"
                                  "{\n"
                                  "    background:transparent\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.imgDir.setText("")
        self.imgDir.setFrame(False)
        self.imgDir.setObjectName("imgDir")
        self.ImageDirLayout.addWidget(self.browseBoxTesting_1)
        self.TestingLayout.addLayout(self.ImageDirLayout, 1, 0, 1, 2)
        self.gridLayout_3.addLayout(self.TestingLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Testing)
        self.mainLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.mainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 21))
        self.menubar.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                                   "selection-color: rgb(0, 0, 0);\n"
                                   "selection-background-color: rgb(154, 201, 254);\n"
                                   "")
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionTrain_Learner = QtWidgets.QAction(MainWindow)
        self.actionTrain_Learner.setObjectName("actionTrain")
        self.actionTesting = QtWidgets.QAction(MainWindow)
        self.actionTesting.setObjectName("actionTesting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionTrain_Guide = QtWidgets.QAction(MainWindow)
        self.actionTrain_Guide.setObjectName("actionTrain_Guide")
        self.actionTest_Guide = QtWidgets.QAction(MainWindow)
        self.actionTest_Guide.setObjectName("actionTest_Guide")
        self.menu_file.addAction(self.actionTrain_Guide)
        self.menu_file.addAction(self.actionTest_Guide)
        self.menu_file.addAction(self.actionTrain_Learner)
        self.menu_file.addAction(self.actionTesting)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionExit)
        self.menu_Help.addAction(self.actionHow_to_use)
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(self.Page.WELCOME.value)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browseBtnImgTesting.clicked.connect(partial(controller.browseImageClicked))
        self.actionAbout.triggered.connect(partial(controller.switch_content, self.Page.ABOUT.value))
        self.actionTrain_Guide.triggered.connect(partial(controller.switch_content, self.Page.TRAIN_GUIDE.value, "Training Guide"))
        self.actionTest_Guide.triggered.connect(partial(controller.switch_content, self.Page.TEST_GUIDE.value, "Testing Guide"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.faceRecTitle.setText(_translate("MainWindow", "Face Recognition"))
        self.faceRecImage.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><img  src=\":/WelcomeImage/welcom.png\"/></p></body></html>"))
        self.customizeTextboxTraining.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/Dir/textInsert.png\"/></p></body></html>"))
        self.trainingDir.setPlaceholderText(_translate("MainWindow", "Training directory"))
        self.title.setText(_translate("MainWindow", "Training"))
        self.customizeTextboxModelTesting.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/Dir/textInsert.png\"/></p></body></html>"))
        self.modelDir.setPlaceholderText(_translate("MainWindow", "Model directory"))
        # self.testingTitle.setText(_translate("MainWindow", "Testing "))
        self.customizeTextboxImgTesting.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/Dir/textInsert.png\"/></p></body></html>"))
        self.imgDir.setPlaceholderText(_translate("MainWindow", "Image directory"))
        self.menu_file.setTitle(_translate("MainWindow", "&Modes"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionTrain_Learner.setText(_translate("MainWindow", "Train Learner"))
        self.actionTesting.setText(_translate("MainWindow", "Test Learner"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionTrain_Guide.setText(_translate("MainWindow", "Train Guide"))
        self.actionTest_Guide.setText(_translate("MainWindow", "Test Guide"))
