# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/resources/qt files/about_with_box2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(460, 354)
        aboutDialog.setMinimumSize(QtCore.QSize(460, 354))
        aboutDialog.setBaseSize(QtCore.QSize(30, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        self.gridLayout_5 = QtWidgets.QGridLayout(aboutDialog)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.mainLayout.setObjectName("mainLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(40, -1, 40, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.contentLayout = QtWidgets.QHBoxLayout()
        self.contentLayout.setObjectName("contentLayout")
        self.content = QtWidgets.QTextBrowser(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.icon_4 = QtWidgets.QLabel(aboutDialog)
        self.icon_4.setObjectName("icon_4")
        self.gridLayout_4.addWidget(self.icon_4, 0, 0, 1, 1)
        self.titleLayout_4 = QtWidgets.QVBoxLayout()
        self.titleLayout_4.setSpacing(0)
        self.titleLayout_4.setObjectName("titleLayout_4")
        self.title_4 = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_4.sizePolicy().hasHeightForWidth())
        self.title_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(28)
        self.title_4.setFont(font)
        self.title_4.setObjectName("title_4")
        self.titleLayout_4.addWidget(self.title_4)
        self.release_4 = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.release_4.sizePolicy().hasHeightForWidth())
        self.release_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.release_4.setFont(font)
        self.release_4.setObjectName("release_4")
        self.titleLayout_4.addWidget(self.release_4)
        self.gridLayout_4.addLayout(self.titleLayout_4, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.mainLayout.addLayout(self.gridLayout)
        self.ok = QtWidgets.QPushButton(aboutDialog)
        self.ok.setObjectName("ok")
        self.mainLayout.addWidget(self.ok, 0, QtCore.Qt.AlignRight)
        self.gridLayout_5.addLayout(self.mainLayout, 0, 0, 1, 1)

        self.retranslateUi(aboutDialog)
        self.ok.clicked.connect(aboutDialog.exec)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About Face Recognition"))
        self.content.setHtml(_translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Copyright © 2018-2019. All Rights Reserved.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">This software was developed in Python 3.6.2. It uses libraries from the PyQt and Tensorflow project, therefore this software is cross-platform.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Third Party, source code and comprehensive explanation on the software can be found at </span><a href=\"https://github.com/adiarbili/FinalProject\"><span style=\" text-decoration: underline; color:#0000ff;\">Face Recognition Project</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; text-decoration: underline;\">Developed by:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Adi Arbili - adiarbili@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Sagi Nof - nof.sagi@gmail.com</span></p></body></html>"))
        self.icon_4.setText(_translate("aboutDialog", "<html><head/><body><p><img src=\":/Icon/icon.ico\" width=\"50\" height=\"50\"/></p></body></html>"))
        self.title_4.setText(_translate("aboutDialog", "Face Recognition"))
        self.release_4.setText(_translate("aboutDialog", "Continuous Release | Version 1.0.0.1"))
        self.ok.setText(_translate("aboutDialog", "OK"))

import guiResourceResource

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutDialog = QtWidgets.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

