# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/resources/qt files/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        self.stackedWidget.addWidget(self.Training)




        self.stackedWidget.addWidget(self.Testing)
        self.mainLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.mainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 26))
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
        self.stackedWidget.setCurrentIndex(2)
        self.actionExit.triggered.connect(MainWindow.close) ##########################################
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.faceRecTitle.setText(_translate("MainWindow", "Face Recognition"))
        self.faceRecImage.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><img  src=\":/WelcomeImage/welcom.png\"/></p></body></html>"))
        self.customizeTextboxTraining.setProperty("class", _translate("MainWindow", "dir"))
        self.trainingDir.setPlaceholderText(_translate("MainWindow", "Training directory"))
        self.trainingTitle.setText(_translate("MainWindow", "Training"))
        self.testingTitle.setText(_translate("MainWindow", "Testing "))
        self.customizeTextboxModelTesting.setProperty("class", _translate("MainWindow", "dir"))
        self.modelDir.setPlaceholderText(_translate("MainWindow", "Model directory"))
        self.customizeTextboxImgTesting.setProperty("class", _translate("MainWindow", "dir"))
        self.imgDir.setPlaceholderText(_translate("MainWindow", "Image directory"))
        self.menu_file.setTitle(_translate("MainWindow", "&Modes"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionTrain_Learner.setText(_translate("MainWindow", "Train Learner"))
        self.actionTesting_Learner.setText(_translate("MainWindow", "Test Learner"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionTrain_Guide.setText(_translate("MainWindow", "Train Guide"))
        self.actionTest_Guide.setText(_translate("MainWindow", "Test Guide"))


import guiResourceResource
