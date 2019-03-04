# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Views import guiResource
from enum import Enum

class Page(Enum):
    WELCOME = 0
    TRAINING = 1
    IDENTIFICATION = 2
    ABOUT = 3


class MainWindow(object):
    def setupUi(self, MainWindow, controller):
        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(690, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(690, 494))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet("")
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 691, 491))
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Welcome = QtWidgets.QWidget()
        self.Welcome.setObjectName("Welcome")
        self.faceRecIcon = QtWidgets.QLabel(self.Welcome)
        self.faceRecIcon.setGeometry(QtCore.QRect(50, 80, 581, 401))
        self.faceRecIcon.setObjectName("faceRecIcon")
        self.faceRecTitle = QtWidgets.QLabel(self.Welcome)
        self.faceRecTitle.setGeometry(QtCore.QRect(150, 30, 351, 81))
        self.faceRecTitle.setObjectName("faceRecTitle")
        self.stackedWidget.addWidget(self.Welcome)
        self.Training = QtWidgets.QWidget()
        self.Training.setObjectName("Training")
        self.browseBox = QtWidgets.QGroupBox(self.Training)
        self.browseBox.setGeometry(QtCore.QRect(20, 100, 421, 60))
        self.browseBox.setStyleSheet("border-style: none")
        self.browseBox.setTitle("")
        self.browseBox.setFlat(False)
        self.browseBox.setCheckable(False)
        self.browseBox.setObjectName("browseBox")
        self.browseBtn = QtWidgets.QPushButton(self.browseBox)
        self.browseBtn.setGeometry(QtCore.QRect(319, 7, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtn.sizePolicy().hasHeightForWidth())
        self.browseBtn.setSizePolicy(sizePolicy)
        self.browseBtn.setStyleSheet("QPushButton#browseBtn:hover\n"
"{\n"
"    image: url(:/BrowseBtn/browseHover.png);\n"
"\n"
"}\n"
"\n"
"QPushButton#browseBtn:pressed\n"
"{\n"
"    image: url(:/BrowseBtn/browsePush.png);\n"
"\n"
"}\n"
"\n"
"QPushButton#browseBtn\n"
"{\n"
"    image: url(:/BrowseBtn/browseDef.png);\n"
"    background:transparent;\n"
"\n"
"}")
        self.browseBtn.setText("")
        self.browseBtn.setIconSize(QtCore.QSize(10, 10))
        self.browseBtn.setAutoRepeatDelay(4)
        self.browseBtn.setAutoRepeatInterval(4)
        self.browseBtn.setObjectName("browseBtn")
        self.dirImage = QtWidgets.QLabel(self.browseBox)
        self.dirImage.setGeometry(QtCore.QRect(4, 10, 311, 41))
        self.dirImage.setObjectName("dirImage")
        self.lineEdit = QtWidgets.QLineEdit(self.browseBox)
        self.lineEdit.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("QLineEdit \n"
"{\n"
"    background:transparent\n"
"}\n"
"\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.trainBtn = QtWidgets.QPushButton(self.Training)
        self.trainBtn.setGeometry(QtCore.QRect(514, 418, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainBtn.sizePolicy().hasHeightForWidth())
        self.trainBtn.setSizePolicy(sizePolicy)
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
        self.trainingTitle = QtWidgets.QLabel(self.Training)
        self.trainingTitle.setGeometry(QtCore.QRect(150, 10, 311, 71))
        self.trainingTitle.setObjectName("trainingTitle")
        self.statusBar = QtWidgets.QLabel(self.Training)
        self.statusBar.setGeometry(QtCore.QRect(5, 447, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        self.stackedWidget.addWidget(self.Training)
        self.Testing = QtWidgets.QWidget()
        self.Testing.setObjectName("Testing")
        self.label = QtWidgets.QLabel(self.Testing)
        self.label.setGeometry(QtCore.QRect(269, 24, 141, 71))
        self.label.setObjectName("label")
        self.testBtn = QtWidgets.QPushButton(self.Testing)
        self.testBtn.setGeometry(QtCore.QRect(604, 430, 80, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testBtn.sizePolicy().hasHeightForWidth())
        self.testBtn.setSizePolicy(sizePolicy)
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
        self.statusBar_2 = QtWidgets.QLabel(self.Testing)
        self.statusBar_2.setGeometry(QtCore.QRect(5, 447, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusBar_2.setFont(font)
        self.statusBar_2.setObjectName("statusBar_2")
        self.label_2 = QtWidgets.QLabel(self.Testing)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 261, 261))
        self.label_2.setStyleSheet("QLabel#label_2\n"
"{\n"
"    #border: 2px solid gray;\n"
"   #border-radius: 130px;\n"
"    #selection-background-color: darkgray;\n"
"    #shadow : 10px 10px 5px grey;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.browseBoxTesting = QtWidgets.QGroupBox(self.Testing)
        self.browseBoxTesting.setGeometry(QtCore.QRect(20, 100, 421, 60))
        self.browseBoxTesting.setStyleSheet("border-style: none")
        self.browseBoxTesting.setTitle("")
        self.browseBoxTesting.setFlat(False)
        self.browseBoxTesting.setCheckable(False)
        self.browseBoxTesting.setObjectName("browseBoxTesting")
        self.browseBtnTesting = QtWidgets.QPushButton(self.browseBoxTesting)
        self.browseBtnTesting.setGeometry(QtCore.QRect(319, 7, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnTesting.sizePolicy().hasHeightForWidth())
        self.browseBtnTesting.setSizePolicy(sizePolicy)
        self.browseBtnTesting.setStyleSheet("QPushButton#browseBtnTesting:hover\n"
"{\n"
"    image: url(:/BrowseBtn/browseHover.png);\n"
"\n"
"}\n"
"\n"
"QPushButton#browseBtnTesting:pressed\n"
"{\n"
"    image: url(:/BrowseBtn/browsePush.png);\n"
"\n"
"}\n"
"\n"
"QPushButton#browseBtnTesting\n"
"{\n"
"    image: url(:/BrowseBtn/browseDef.png);\n"
"    background:transparent;\n"
"\n"
"}")
        self.browseBtnTesting.setText("")
        self.browseBtnTesting.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnTesting.setAutoRepeatDelay(4)
        self.browseBtnTesting.setAutoRepeatInterval(4)
        self.browseBtnTesting.setObjectName("browseBtnTesting")
        self.dirImageTesting = QtWidgets.QLabel(self.browseBoxTesting)
        self.dirImageTesting.setGeometry(QtCore.QRect(4, 10, 311, 41))
        self.dirImageTesting.setObjectName("dirImageTesting")
        self.lineEditTesting = QtWidgets.QLineEdit(self.browseBoxTesting)
        self.lineEditTesting.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditTesting.setFont(font)
        self.lineEditTesting.setAutoFillBackground(False)
        self.lineEditTesting.setStyleSheet("QLineEdit \n"
"{\n"
"    background:transparent\n"
"}\n"
"\n"
"")
        self.lineEditTesting.setText("")
        self.lineEditTesting.setFrame(False)
        self.lineEditTesting.setObjectName("lineEditTesting")
        self.stackedWidget.addWidget(self.Testing)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
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
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")

        # self.menubar.triggered[QtWidgets.QAction].connect(controller.switch_content)

        self.actionTrain.triggered.connect(partial(controller.switch_content, Page.TRAINING.value))
        # self.actionTrain.triggered.connect(controller.switch_content)
        # print(self.menubar.triggered[QtWidgets.QAction])
################################################################################################


        self.actionTesting = QtWidgets.QAction(MainWindow)
        self.actionTesting.setObjectName("actionTesting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_file.addAction(self.actionTrain)
        self.menu_file.addAction(self.actionTesting)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionExit)
        self.menu_Help.addAction(self.actionHow_to_use)
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browseBtnTesting.clicked.connect(partial(controller.browseImageClicked))
        self.actionAbout.triggered.connect(partial(controller.switch_content, Page.ABOUT.value))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.faceRecIcon.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img  src=\":/WelcomeImage/welcom.png\"/></p></body></html>"))
        self.faceRecTitle.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"350\" height=\"80\" src=\":/WelcomeTitle/welcomeTitle.png\"/></p></body></html>"))
        self.dirImage.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Dir/textInsert.png\"/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Training directory"))
        self.trainingTitle.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/TrainingTitle/trainingTitle.png\"/></p></body></html>"))
        self.statusBar.setText(_translate("MainWindow", "Status bar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/TestingTitle/testingTitle.png\"/></p></body></html>"))
        self.statusBar_2.setText(_translate("MainWindow", "Status bar"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"261\" height=\"261\"  src=\":/DefaultImage/defualtImage.png\"/></p></body></html>"))
        self.dirImageTesting.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Dir/textInsert.png\"/></p></body></html>"))
        self.lineEditTesting.setPlaceholderText(_translate("MainWindow", "Image directory"))
        self.menu_file.setTitle(_translate("MainWindow", "&Modes"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionTrain.setText(_translate("MainWindow", "Training"))
        self.actionTesting.setText(_translate("MainWindow", "Testing"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


