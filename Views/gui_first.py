# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Views import guiResource
import sys
from Inception import hello


class MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(682, 443)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/WelcomeImage/face_recognition_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet("background-color: rgb(124, 154, 166);")
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 691, 421))
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")

        self.Welcome = QtWidgets.QWidget()
        self.Welcome.setObjectName("Welcome")

        self.faceRecIcon = QtWidgets.QLabel(self.Welcome)
        self.faceRecIcon.setGeometry(QtCore.QRect(220, 130, 241, 241))
        self.faceRecIcon.setObjectName("faceRecIcon")

        self.faceRecTitle = QtWidgets.QLabel(self.Welcome)
        self.faceRecTitle.setGeometry(QtCore.QRect(150, 30, 351, 81))
        self.faceRecTitle.setObjectName("faceRecTitle")

        self.stackedWidget.addWidget(self.Welcome)

        self.Training = QtWidgets.QWidget()
        self.Training.setObjectName("Training")

        self.browseBox = QtWidgets.QGroupBox(self.Training)
        self.browseBox.setGeometry(QtCore.QRect(20, 100, 411, 60))
        self.browseBox.setStyleSheet("border-style: none")
        self.browseBox.setTitle("")
        self.browseBox.setFlat(False)
        self.browseBox.setCheckable(False)
        self.browseBox.setObjectName("browseBox")
        self.browseBtn = QtWidgets.QPushButton(self.browseBox)
        self.browseBtn.setGeometry(QtCore.QRect(320, 1, 81, 61))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtn.sizePolicy().hasHeightForWidth())

        self.browseBtn.setSizePolicy(sizePolicy)
        self.browseBtn.setStyleSheet("""QPushButton#browseBtn:hover
                                    {image: url(:/BrowseBtn/browseHover.png);}
                                    QPushButton#browseBtn:pressed
                                    {image: url(:/BrowseBtn/browsePush.png);}
                                    QPushButton#browseBtn
                                    {image: url(:/BrowseBtn/browseDef.png);
                                    background:transparent;}""")
        self.browseBtn.setText("")
        self.browseBtn.setIconSize(QtCore.QSize(10, 10))
        self.browseBtn.setAutoRepeatDelay(4)
        self.browseBtn.setAutoRepeatInterval(4)
        self.browseBtn.setObjectName("browseBtn")

        self.dirImage = QtWidgets.QLabel(self.browseBox)
        self.dirImage.setGeometry(QtCore.QRect(4, 10, 311, 41))
        self.dirImage.setObjectName("dirImage")
        self.lineEdit = QtWidgets.QLineEdit(self.browseBox)
        self.lineEdit.setGeometry(QtCore.QRect(11, 16, 291, 31))
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
        self.trainBtn.setGeometry(QtCore.QRect(508, 365, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainBtn.sizePolicy().hasHeightForWidth())
        self.trainBtn.setSizePolicy(sizePolicy)
        self.trainBtn.setStyleSheet("""QPushButton#trainBtn:hover
                                    {image: url(:/StartTrainingBtn/startTrainingHover.png);}
                                    QPushButton#trainBtn:pressed
                                    {image: url(:/StartTrainingBtn/startTrainingPush.png);}
                                    QPushButton#trainBtn
                                    {image: url(:/StartTrainingBtn/startTrainingDef.png);
                                     background:transparent;}""")

        self.trainBtn.setText("")
        self.trainBtn.setIconSize(QtCore.QSize(10, 10))
        self.trainBtn.setAutoRepeatDelay(4)
        self.trainBtn.setAutoRepeatInterval(4)
        self.trainBtn.setObjectName("trainBtn")
        self.trainingTitle = QtWidgets.QLabel(self.Training)
        self.trainingTitle.setGeometry(QtCore.QRect(150, 10, 311, 71))
        self.trainingTitle.setObjectName("trainingTitle")
        self.statusBar = QtWidgets.QLabel(self.Training)
        self.statusBar.setGeometry(QtCore.QRect(3, 388, 491, 31))
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

        self.groupBrowseTesting = QtWidgets.QGroupBox(self.Testing)
        self.groupBrowseTesting.setGeometry(QtCore.QRect(10, 100, 411, 60))
        self.groupBrowseTesting.setStyleSheet("border-style: none")
        self.groupBrowseTesting.setTitle("")
        self.groupBrowseTesting.setFlat(False)
        self.groupBrowseTesting.setCheckable(False)
        self.groupBrowseTesting.setObjectName("groupBrowseTesting")
        self.browseBtnTesting = QtWidgets.QPushButton(self.groupBrowseTesting)
        self.browseBtnTesting.setGeometry(QtCore.QRect(320, 1, 81, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnTesting.sizePolicy().hasHeightForWidth())
        self.browseBtnTesting.setSizePolicy(sizePolicy)
        self.browseBtnTesting.setStyleSheet("\n"
                                            "QPushButton#browseBtnTesting:hover\n"
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
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.browseBtnTesting.setText("")
        self.browseBtnTesting.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnTesting.setAutoRepeatDelay(4)
        self.browseBtnTesting.setAutoRepeatInterval(4)
        self.browseBtnTesting.setObjectName("browseBtnTesting")
        self.imgDirTesting = QtWidgets.QLabel(self.groupBrowseTesting)
        self.imgDirTesting.setGeometry(QtCore.QRect(4, 10, 311, 41))
        self.imgDirTesting.setObjectName("imgDirTesting")
        self.textImgDirTesting = QtWidgets.QLineEdit(self.groupBrowseTesting)
        self.textImgDirTesting.setGeometry(QtCore.QRect(11, 16, 291, 31))
        self.textImgDirTesting.setAutoFillBackground(False)
        self.textImgDirTesting.setStyleSheet("QLineEdit \n"
                                             "{\n"
                                             "    background:transparent\n"
                                             "}\n"
                                             "\n"
                                             "")
        self.textImgDirTesting.setText("")
        self.textImgDirTesting.setFrame(False)
        self.textImgDirTesting.setObjectName("textImgDirTesting")
        self.frame = QtWidgets.QFrame(self.Testing)
        self.frame.setGeometry(QtCore.QRect(40, 170, 251, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.testBtn = QtWidgets.QPushButton(self.Testing)
        self.testBtn.setGeometry(QtCore.QRect(598, 377, 80, 41))
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
                                   "")
        self.testBtn.setText("")
        self.testBtn.setIconSize(QtCore.QSize(10, 10))
        self.testBtn.setAutoRepeatDelay(4)
        self.testBtn.setAutoRepeatInterval(4)
        self.testBtn.setObjectName("testBtn")
        self.statusBar_2 = QtWidgets.QLabel(self.Testing)
        self.statusBar_2.setGeometry(QtCore.QRect(5, 391, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusBar_2.setFont(font)
        self.statusBar_2.setObjectName("statusBar_2")
        self.stackedWidget.addWidget(self.Testing)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setStyleSheet("""background-color: rgb(231, 231, 231);
                                   selection-color: rgb(0, 0, 0);
                                   selection-background-color: rgb(154, 201, 254);
                                   """)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)

        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionTrain.triggered.connect(partial(self.swtich_content, 1))
        # self.actionTrain.triggered.connect(lambda: self.swtich_content(1))

        self.actionTesting = QtWidgets.QAction(MainWindow)
        self.actionTesting.setObjectName("actionTesting")
        self.actionTesting.triggered.connect(partial(self.swtich_content, 2))

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(MainWindow.close)

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
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.faceRecIcon.setText(_translate("MainWindow",
                                            "<html><head/><body><p><img width=\"240\" height=\"240\" src=\":/WelcomeImage/face_recognition_icon.png\"/></p></body></html>"))
        self.faceRecTitle.setText(_translate("MainWindow",
                                             "<html><head/><body><p><img width=\"350\" height=\"80\" src=\":/WelcomeTitle/welcomeTitle.png\"/></p></body></html>"))
        self.dirImage.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/Dir/textInsert.png\"/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Training directory"))
        self.trainingTitle.setText(_translate("MainWindow",
                                              "<html><head/><body><p><img src=\":/TrainingTitle/trainingTitle.png\"/></p></body></html>"))
        self.statusBar.setText(_translate("MainWindow", "Status bar"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><img src=\":/TestingTitle/testingTitle.png\"/></p></body></html>"))
        self.imgDirTesting.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/Dir/textInsert.png\"/></p></body></html>"))
        self.textImgDirTesting.setPlaceholderText(_translate("MainWindow", "Image directory"))
        self.statusBar_2.setText(_translate("MainWindow", "Status bar"))
        self.menu_file.setTitle(_translate("MainWindow", "&Modes"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionTrain.setText(_translate("MainWindow", "Training"))
        self.actionTesting.setText(_translate("MainWindow", "Testing"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def swtich_content(self, num):
        print(num)
        hello.printHello()
        if num < 3:
            self.stackedWidget.setCurrentIndex(num)

