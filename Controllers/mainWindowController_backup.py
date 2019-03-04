from PyQt5.QtWidgets import  QFileDialog, QDialog
from PyQt5.QtGui import  QPixmap, QPainter, QPainterPath
from PyQt5 import  QtWidgets
import sys
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath, QBrush, QImage, QPainter, QPixmap, QWindow, QColor, QPen
from Views import aboutView
# from View import About4



class MainWindowController:

    def __init__(self):
        pass

    def setGui(self, gui):
        self.gui = gui

    def switch_content(self, page, title=''):
        # print(num.text())
        if page < self.gui.Page.ABOUT.value:
            if page ==self.gui.Page.TRAIN_GUIDE.value:
                self.gui.trainingTitle.setText(title)
            elif page == self.gui.Page.TEST_GUIDE.value:
                    self.gui.testingTitle.setText(title)

            self.gui.stackedWidget.setCurrentIndex(page)
        else:
            if page == self.gui.Page.ABOUT.value:
                about = about.aboutDialog()
                dialog = QDialog(self.gui.MainWindow, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
                about.setupUi(dialog)
                dialog.exec()
            elif page == self.gui.Page.HOW_TO_USE.value:
                about = about.aboutDialog()
                dialog = QDialog(self.gui.MainWindow, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
                about.setupUi(dialog)
                dialog.exec()


    def browseImageClicked(self):
        file_name = QFileDialog.getOpenFileName(None, 'Choose an image', '', 'Image files (*.jpg *.png *.bmp)')

        if file_name[0]:
            self.gui.imgDir.setText(file_name[0])

            # imageData = open("C:/Adi/Projects/Face Recognition/testing_data/cats/cat.1000.jpg", 'rb').read()
            imgsize = 160

            imageData = open(file_name[0], 'rb').read()

            image = QImage.fromData(imageData, "jpg")

            image.convertToFormat(QImage.Format_ARGB32)

            image = image.scaled(imgsize,imgsize,Qt.IgnoreAspectRatio)
            print(image.width())
            print(image.height())


            # Crop image to a square:
            #
            # rect = QRect(
            #     # (image.width() - imgsize) / 2,
            #     # (image.height() - imgsize) / 2,
            #     0,
            #     0,
            #     imgsize,
            #     imgsize,
            # )
            # image = image.copy(rect)

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
            # painter.setPen(Qt.NoPen)  # Don't draw an outline
            painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
            painter.drawEllipse(2, 2, imgsize-4, imgsize-4)  # Actually draw the circle
            painter.end()  # We are done (segfault if you forget this)

            # Convert the image to a pixmap and rescale it.  Take pixel ratio into
            # account to get a sharp image on retina displays:
            pr = QWindow().devicePixelRatio()
            pm = QPixmap.fromImage(out_img)
            pm.setDevicePixelRatio(pr)
            size = 200*pr
            # pm = pm.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            pm = pm.scaled(self.gui.chosenImg.width(), self.gui.chosenImg.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # pm = pm.scaled(size, self.gui.label_2.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.gui.chosenImg.setPixmap(pm)
            # self.gui.label_2.alignment()

            # print(self.gui.chosenImg.width())