import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Controllers.mainController import MainController
from Views.mainView import MainView


def runApp():
    app = QApplication(sys.argv)
    mainController = MainController()
    window = QMainWindow()
    ui = MainView()
    ui.setupUi(window, mainController)
    mainController.setView(ui)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    runApp()
