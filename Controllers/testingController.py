from Controllers.controller import Controller

import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QImage, QPainter, QPen, QPixmap, QWindow
from PyQt5.QtWidgets import QFileDialog

from threading import Thread


class TestingController(Controller):
    testingDirImageValid = False

    def __init__(self):
        super()

    def browseImageBtnClicked(self):
        file_name = QFileDialog.getOpenFileName(None, 'Choose an image', '', 'Image files (*.jpg *.png *.bmp)')

        if file_name[0]:
            self.view.imgDir.setText(file_name[0])
            self.testingDirImageValid = True
            self.setStatusBarMessage("Image loaded successfully")
        else:
            self.testingDirImageValid = False

    def imgDirChanges(self):
        self.selectionDirChanges(self.view.imgDir)

        if os.path.isfile(self.view.imgDir.text()):
            self.dispalyCircularImage(self.view.imgDir.text())
            self.testingDirImageValid = True
        elif self.testingDirImageValid:
            self.view.chosenImg.clear()
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
        pm = pm.scaled(self.view.chosenImg.width(), self.view.chosenImg.height(), Qt.KeepAspectRatio,
                       Qt.SmoothTransformation)
        # pm = pm.scaled(size, self.view.label_2.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.view.chosenImg.setPixmap(pm)

    def startTestingGuide(self):
        if not os.path.isdir(self.view.modelDir.text()):
            self._Controller__invalidPath(self.view.modelDir)
            self.setStatusBarMessage("Invalid Model directory")
        elif not self.testingDirImageValid:
            self._Controller__invalidPath(self.view.imgDir)
            self.setStatusBarMessage("Invalid image directory")
        else:
            # start testing process
            self.setStatusBarMessage("Starting testing process")
            try:
                testing_thread = Thread(target=self.__printX, daemon=True)  # daemon=None - means inherited
                testing_thread.start()
            except:
                print("Error: unable to start thread")
                self.setStatusBarMessage("Unknown error: unable to start testing process")

    def __printX(self):
        for i in range(99999999):
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaa {}".format(i))
