# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/resources/qt files/about_origin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Views import guiResource

class About(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(422, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutDialog.sizePolicy().hasHeightForWidth())
        aboutDialog.setSizePolicy(sizePolicy)
        aboutDialog.setMinimumSize(QtCore.QSize(0, 360))
        aboutDialog.setMaximumSize(QtCore.QSize(422, 360))
        aboutDialog.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(aboutDialog)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.mainLayout.setObjectName("mainLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.contentLayout = QtWidgets.QHBoxLayout()
        self.contentLayout.setObjectName("contentLayout")
        self.content = QtWidgets.QTextBrowser(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setStyleSheet("background: transparent;")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setOpenExternalLinks(True)
        self.content.setObjectName("content")
        self.contentLayout.addWidget(self.content)
        self.gridLayout.addLayout(self.contentLayout, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(aboutDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.icon = QtWidgets.QLabel(aboutDialog)
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.titleLayout = QtWidgets.QVBoxLayout()
        self.titleLayout.setSpacing(0)
        self.titleLayout.setObjectName("titleLayout")
        self.title = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.titleLayout.addWidget(self.title)
        self.release = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.release.sizePolicy().hasHeightForWidth())
        self.release.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.release.setFont(font)
        self.release.setObjectName("release")
        self.titleLayout.addWidget(self.release)
        self.gridLayout.addLayout(self.titleLayout, 0, 1, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)
        self.ok = QtWidgets.QPushButton(aboutDialog)
        self.ok.setObjectName("ok")
        self.mainLayout.addWidget(self.ok, 0, QtCore.Qt.AlignRight)
        self.gridLayout_2.addLayout(self.mainLayout, 0, 0, 1, 1)

        self.retranslateUi(aboutDialog)
        self.ok.clicked.connect(aboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

        aboutDialog.setModal(True)
        # aboutDialog.show()
        # aboutDialog.exec()
        x = aboutDialog.parentWidget().x() + (
                aboutDialog.parentWidget().frameGeometry().width() - aboutDialog.frameGeometry().width()) / 2
        y = aboutDialog.parentWidget().y() + (
                aboutDialog.parentWidget().frameGeometry().height() - aboutDialog.frameGeometry().height()) / 2
        aboutDialog.move(x, y)
        # aboutDialog.show()
        print("asd")

        # aboutDialog.resize(422, 360)

        # aboutDialog.exec()
        # aboutDialog.showMinimized()
        # aboutDialog.showNormal()



    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About Face Recognition"))
        self.content.setHtml(_translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Copyright © 2018-2019. All Rights Reserved.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">This software was developed in Python 3.6.8. It uses libraries from the PyQt and Tensorflow project, therefore this software is cross-platform.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Third Party, source code and comprehensive explanations on this software can be found at </span><a href=\"https://github.com/adiarbili/FinalProject\"><span style=\" text-decoration: underline; color:#0000ff;\">Face Recognition Project</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; text-decoration: underline;\">Developed by:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Adi Arbili - adiarbili@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Sagi Nof - nof.sagi@gmail.com</span></p></body></html>"))
        self.icon.setText(_translate("aboutDialog", "<html><head/><body><p><img src=\":/Icon/icon.ico\" width=\"50\" height=\"50\"/></p></body></html>"))
        self.title.setText(_translate("aboutDialog", "Face Recognition"))
        self.release.setText(_translate("aboutDialog", "Continuous Release | Version 1.0.0"))
        self.ok.setText(_translate("aboutDialog", "OK"))



