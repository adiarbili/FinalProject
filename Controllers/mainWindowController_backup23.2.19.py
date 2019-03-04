from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath, QBrush, QImage, QPainter, QPixmap, QWindow, QColor, QPen
from Views import aboutView
import os


class MainWindowController:
    trainingDatasetDirValid = False
    testingDirModelValid = False
    testingDirImageValid = False
    timeout = 5000

    def __init__(self):
        self.about = None
        pass

    def setGui(self, gui):
        self.gui = gui

    def switch_content(self, page, title=''):
        # self.gui.mainWindow.resize(524, 0)
        # self.gui.mainWindow.resize(524, 0)
        # print("width={}".format(self.gui.mainWindow.width()))
        # print("height={}".format(self.gui.mainWindow.height()))

        if page < self.gui.Page.ABOUT.value:
            # if page == self.gui.Page.TRAIN_GUIDE.value:
            #     self.gui.trainingTitle.setText(title)
            # elif page == self.gui.Page.TEST_GUIDE.value:
            #     self.gui.testingTitle.setText(title)

            self.gui.stackedWidget.setCurrentIndex(page)
        else:
            if page == self.gui.Page.ABOUT.value:
                # if self.about is None:
                self.about = about.aboutDialog()
                self.dialog = QDialog(self.gui.mainWindow, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
                self.about.setupUi(self.dialog)
                # print("width={}".format(dialog.width()))
                # print("height={}".format(dialog.height()))
                self.dialog.exec()
            elif page == self.gui.Page.HOW_TO_USE.value:
                about = about.aboutDialog()
                dialog = QDialog(self.gui.mainWindow, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
                about.setupUi(dialog)
                dialog.exec()

        # print("width={}".format(self.gui.mainWindow.width()))
        # print("height={}".format(self.gui.mainWindow.height()))

    def browseImageBtnClicked(self):
        file_name = QFileDialog.getOpenFileName(None, 'Choose an image', '', 'Image files (*.jpg *.png *.bmp)')

        if file_name[0]:
            self.gui.imgDir.setText(file_name[0])
            testingDirImageValid = True
        else:
            testingDirImageValid = False

    def browseDirBtnClicked(self, target):
        file_name = QFileDialog.getExistingDirectory(None, 'Choose a directory')

        if file_name:
            # self.gui.modelDir.setText(file_name)
            target.setText(file_name)

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

    def selectionDirChanges(self, textbox, mode):
        if textbox.property("invalid"):
            textbox.setProperty("invalid", False)
            self.validPath(textbox)
        # if
        #     self.setStatusBarMessage("Image model/training directory successfully")

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

    def startTrainingGuide(self):
        if not os.path.isdir(self.gui.trainingDir.text()):
            self.invalidPath(self.gui.trainingDir)
            self.setStatusBarMessage("Invalid training directory")
        else:
            self.setStatusBarMessage("Start training process")
            # startTraining

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
            # startTesting

    def setStatusBarMessage(self, msg):
        self.gui.statusBar.showMessage(msg, self.timeout)

    def invalidPath(self, widget):
        widget.setFocus()
        widget.setProperty("invalid", True)
        self.updateWidgetStyleSheet(widget)

    def validPath(self, widget):
        widget.setProperty("invalid", False)
        self.updateWidgetStyleSheet(widget)

    def updateWidgetStyleSheet(self, widget):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
