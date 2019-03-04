
from PyQt5.QtWidgets import QFileDialog
from Controllers.mainController import MainController


class Controller:

    def setView(self, view):
        self.view = view

    def browseDirBtnClicked(self, target, successfullMsg):
        file_name = QFileDialog.getExistingDirectory(None, 'Choose a directory')

        if file_name:
            target.setText(file_name)
            self.setStatusBarMessage(successfullMsg)

    def selectionDirChanges(self, textbox):
        if textbox.property("invalid"):
            textbox.setProperty("invalid", False)
            self.__validPath(textbox)

    def setStatusBarMessage(self, msg):
        MainController.setStatusBarMessage(msg)

    def __invalidPath(self, widget):
        widget.setFocus()
        widget.setProperty("invalid", True)
        self.__updateWidgetStyleSheet(widget)

    def __validPath(self, widget):
        widget.setProperty("invalid", False)
        self.__updateWidgetStyleSheet(widget)

    def __updateWidgetStyleSheet(self, widget):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
