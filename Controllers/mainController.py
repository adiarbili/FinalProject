from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from Views.aboutView import About
from Views.about2 import Ui_aboutDialog


class MainController:
    __timeout = 5000

    __statusBar = None

    def __init__(self):
        self.about = None
        pass

    def setView(self, view):
        self.view = view
        MainController.__statusBar = self.view.statusBar
    def close(self):
        content = 'Training process is still running.\n' \
                  'Clicking on "Yes" will terminate the process,\n' \
                  'Are you sure?'
        closeBox = QMessageBox.question(self.view.mainWindow, "Face Recognition", content,
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

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
