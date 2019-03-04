from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath, QBrush, QImage, QPainter, QPixmap, QWindow, QColor, QPen
from Views.aboutView import About
from Views.about2 import Ui_aboutDialog
from PyQt5 import QtCore
import os

# from Controllers.controller import Controller

class MainController:
    __timeout = 5000
    trainingDatasetDirValid = False
    testingDirModelValid = False
    testingDirImageValid = False
    __statusBar = None

    def __init__(self):
        self.about = None
        pass

    def setView(self, view):
        self.view = view
        MainController.__statusBar = self.view.statusBar

    def close(self):
        _translate = QtCore.QCoreApplication.translate

        content = """
                    Face Recognition
                    Continuous Release | Version 1.0.0
                        
                    Copyright © 2018-2019. All Rights Reserved.
                    
                    This software was developed in Python 3.6.2. It uses libraries from the PyQt and Tensorflow project, therefore this software is cross-platform.
                    
                    Third Party, source code and comprehensive explanation on the software can be found at Face Recognition Project
                    
                    Developed by:
                    
                    Adi Arbili - adiarbili@gmail.com
                    Sagi Nof - nof.sagi@gmail.com
        """
        closeBox =  QMessageBox.about(self.view.mainWindow, "About Face Recognition", content)


        content = 'Training process is still running.\n' \
                  'Clicking on "Yes" will terminate training process,\n' \
                  'Are you sure?'
        closeBox = QMessageBox.question(self.view.mainWindow, "Face Recognition", content, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if closeBox == QMessageBox.Yes:
            self.view.mainWindow.close()

    def switch_content(self, page):
        if page < self.view._Page.ABOUT.value:
            self.view.stackedWidget.setCurrentIndex(page)
        else:
            if page == self.view._Page.ABOUT.value:
                # if self.about is None:
                #     self.about = About()
                #     self.dialog = QDialog(self.view.mainWindow, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
                #     self.about.setupUi(self.dialog)
                # self.dialog.exec()


                self.about = Ui_aboutDialog()
                self.dialog = QDialog(self.view.mainWindow, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
                self.about.setupUi(self.dialog)

                self.dialog.show()

            elif page == self.view._Page.HOW_TO_USE.value:
                about = About()
                dialog = QDialog(self.view.mainWindow, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
                about.setupUi(dialog)
                dialog.exec()

    @staticmethod
    def setStatusBarMessage(msg):
        MainController.__statusBar.showMessage(msg, MainController.__timeout)
'''

    def browseImageBtnClicked(self):
        file_name = QFileDialog.getOpenFileName(None, 'Choose an image', '', 'Image files (*.jpg *.png *.bmp)')

        if file_name[0]:
            self.gui.imgDir.setText(file_name[0])
            testingDirImageValid = True
        else:
            testingDirImageValid = False


    def imgDirChanges(self):

        # dispalyCircularImage(self.gui.imgDir.text(), target)
        self.validPath(self.gui.imgDir)

        if os.path.isfile(self.gui.imgDir.text()):
            self.dispalyCircularImage(self.gui.imgDir.text())
            self.testingDirImageValid = True
            self.setStatusBarMessage("Image loaded successfully")
        elif self.testingDirImageValid:
            self.gui.chosenImg.clear()
            self.testingDirImageValid = False



    def dispalyCircularImage(self, imgPath):
        # imageData = open("C:/Adi/Projects/Face Recognition/testing_data/cats/cat.1000.jpg", 'rb').read()
        imgsize = 210

        imageData = open(imgPath, 'rb').read()
        image = QImage.fromData(imageData, "jpg")
        image.convertToFormat(QImage.Format_ARGB32)
        image = image.scaled(imgsize, imgsize, Qt.IgnoreAspectRatio)

        # Create the output image with the same dimensions and an alpha channel
        # and make it completely transparent:
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        # Create a texture brush and paint a circle with the original image onto
        # the output image:
        brush = QBrush(image)  # Create texture brush
        painter = QPainter(out_img)  # Paint the output image
        painter.setBrush(brush)  # Use the image texture brush
        pen = QPen(QColor(255, 255, 255), 2)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
        painter.drawEllipse(2, 2, imgsize - 4, imgsize - 4)  # Actually draw the circle
        painter.end()  # We are done (segfault if you forget this)

        # Convert the image to a pixmap and rescale it.  Take pixel ratio into
        # account to get a sharp image on retina displays:
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        # size = 200*pr
        # pm = pm.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pm = pm.scaled(self.gui.chosenImg.width(), self.gui.chosenImg.height(), Qt.KeepAspectRatio,
                       Qt.SmoothTransformation)
        # pm = pm.scaled(size, self.gui.label_2.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.gui.chosenImg.setPixmap(pm)



    def startTestingGuide(self):

        if not os.path.isdir(self.gui.modelDir.text()):
            self.invalidPath(self.gui.modelDir)
            self.setStatusBarMessage("Invalid model directory")
        elif not self.testingDirImageValid:
            self.invalidPath(self.gui.imgDir)
            self.setStatusBarMessage("Invalid image directory")
        else:
            self.setStatusBarMessage("Start testing process")
            print("Valid")
'''            # startTesting