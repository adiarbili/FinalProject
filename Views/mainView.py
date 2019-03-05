# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/resources/qt files/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from enum import Enum
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

from Controllers.trainingController import TrainingController
from Controllers.testingController import TestingController

from Views.trainingView import TrainingView
from Views.testingView import TestingView
from Views import guiResource


class MainView(object):
    # Page = Enum('WELCOME', 'TRAIN_GUIDE', 'TEST_GUIDE', 'TEST_GUIDE')
    class _Page(Enum):
        WELCOME = 0
        TRAIN_GUIDE = 1
        TEST_GUIDE = 2
        TRAIN_LEARNER = 3
        TEST_LEARNER = 4
        ABOUT = 5
        HOW_TO_USE = 6

    def setupUi(self, MainWindow, controller):
        self.mainWindow = MainWindow
        # MainWindow.move(0,0)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(526, 524)
        # MainWindow.setMinimumSize(526, 124)
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
        self.stackedWidget.setStyleSheet("QLineEdit{\n"
                                         "    background:transparent;\n"
                                         "}\n"
                                         "QLineEdit[invalid = true]{\n"
                                         "    font-weight:1000;\n"
                                         "    color:red;\n"
                                         "    background:transparent;\n"
                                         "}\n"
                                         "QLabel[class = dir]\n"
                                         "{\n"
                                         "    image: url(:/Dir/textInsert.png);\n"
                                         "}")
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

        self.__initViewsAndControllers(TrainingController, "Training Guide", TrainingView)

        self.__initViewsAndControllers(TestingController, "Testing Guide", TestingView)

        # self.testingGuide = TestingView("Testing Guide")
        # self.stackedWidget.addWidget(self.testingGuide.Testing)
        #
        # self.trainingLearner = TrainingView("Training Learner")
        # self.stackedWidget.addWidget(self.trainingLearner.Training)
        #
        # self.testingLearner = TestingView("Testing Learner")
        # self.stackedWidget.addWidget(self.testingLearner.Testing)

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
        # self.statusBar.setMinimumHeight(25)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionTrain_Learner = QtWidgets.QAction(MainWindow)
        self.actionTrain_Learner.setObjectName("actionTrain_Learner")
        self.actionTesting_Learner = QtWidgets.QAction(MainWindow)
        self.actionTesting_Learner.setObjectName("actionTesting_Learner")
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
        self.menu_file.addAction(self.actionTesting_Learner)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionExit)
        self.menu_Help.addAction(self.actionHow_to_use)
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(self._Page.WELCOME.value)
        self.actionExit.triggered.connect(controller.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionAbout.triggered.connect(partial(controller.switch_content, self._Page.ABOUT.value))
        self.actionTrain_Guide.triggered.connect(partial(controller.switch_content, self._Page.TRAIN_GUIDE.value))
        self.actionTest_Guide.triggered.connect(partial(controller.switch_content, self._Page.TEST_GUIDE.value))
        self.actionTrain_Learner.triggered.connect(partial(controller.switch_content, self._Page.TRAIN_LEARNER.value))
        self.actionTesting_Learner.triggered.connect(partial(controller.switch_content, self._Page.TEST_LEARNER.value))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.faceRecTitle.setText(_translate("MainWindow", "Face Recognition"))
        self.faceRecImage.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><img  src=\":/WelcomeImage/welcom.png\"/></p></body></html>"))

        self.menu_file.setTitle(_translate("MainWindow", "&Modes"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionTrain_Learner.setText(_translate("MainWindow", "Train Learner"))
        self.actionTesting_Learner.setText(_translate("MainWindow", "Test Learner"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionTrain_Guide.setText(_translate("MainWindow", "Train Guide"))
        self.actionTest_Guide.setText(_translate("MainWindow", "Test Guide"))

    def __initViewsAndControllers(self, ctrlConstructor, title, viewConstructor):
        controller = ctrlConstructor()
        view = viewConstructor(title, controller)
        controller.setView(view)
        self.stackedWidget.addWidget(view)
