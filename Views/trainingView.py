from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

class TrainingView(QtWidgets.QWidget):
# class TrainingView:
    def __init__(self, title, controller):
        # QtWidgets.QWidget.__init__(self)
        super().__init__()
        self.setObjectName("Training")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)

        # self.Training = QtWidgets.QWidget()
        # self.Training.setObjectName("Training")
        # self.gridLayout_2 = QtWidgets.QGridLayout(self.Training)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.trainingLayout = QtWidgets.QGridLayout()
        self.trainingLayout.setHorizontalSpacing(0)
        self.trainingLayout.setVerticalSpacing(20)
        self.trainingLayout.setObjectName("trainingLayout")
        # self.browseBoxTraining = QtWidgets.QGroupBox(self.Training)
        self.browseBoxTraining = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBoxTraining.sizePolicy().hasHeightForWidth())
        self.browseBoxTraining.setSizePolicy(sizePolicy)
        self.browseBoxTraining.setMinimumSize(QtCore.QSize(0, 60))
        self.browseBoxTraining.setStyleSheet("border-style: none")
        self.browseBoxTraining.setTitle("")
        self.browseBoxTraining.setFlat(False)
        self.browseBoxTraining.setCheckable(False)
        self.browseBoxTraining.setObjectName("browseBoxTraining")
        self.browseBtnTraining = QtWidgets.QPushButton(self.browseBoxTraining)
        self.browseBtnTraining.setGeometry(QtCore.QRect(319, 6, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnTraining.sizePolicy().hasHeightForWidth())
        self.browseBtnTraining.setSizePolicy(sizePolicy)
        self.browseBtnTraining.setStyleSheet("QPushButton#browseBtnTraining:hover\n"
                                             "{\n"
                                             "    image: url(:/BrowseBtn/browseHover.png);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#browseBtnTraining:pressed\n"
                                             "{\n"
                                             "    image: url(:/BrowseBtn/browsePush.png);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#browseBtnTraining\n"
                                             "{\n"
                                             "    image: url(:/BrowseBtn/browseDef.png);\n"
                                             "    background:transparent;\n"
                                             "\n"
                                             "}")
        self.browseBtnTraining.setText("")
        self.browseBtnTraining.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnTraining.setAutoRepeatDelay(4)
        self.browseBtnTraining.setAutoRepeatInterval(4)
        self.browseBtnTraining.setObjectName("browseBtnTraining")
        self.customizeTextboxTraining = QtWidgets.QLabel(self.browseBoxTraining)
        self.customizeTextboxTraining.setGeometry(QtCore.QRect(4, 10, 309, 43))
        self.customizeTextboxTraining.setStyleSheet("")
        self.customizeTextboxTraining.setText("")
        self.customizeTextboxTraining.setObjectName("customizeTextboxTraining")
        self.customizeTextboxTraining.setProperty("class", "dir")
        self.trainingDir = QtWidgets.QLineEdit(self.browseBoxTraining)
        self.trainingDir.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trainingDir.setFont(font)
        self.trainingDir.setAutoFillBackground(False)
        self.trainingDir.setStyleSheet("")
        self.trainingDir.setText("")
        self.trainingDir.setPlaceholderText("Training directory")

        self.trainingDir.setFrame(False)
        self.trainingDir.setObjectName("trainingDir")
        self.customizeTextboxTraining.raise_()
        self.trainingDir.raise_()
        self.browseBtnTraining.raise_()
        self.trainingLayout.addWidget(self.browseBoxTraining, 1, 0, 1, 1)
        # self.trainingTitle = QtWidgets.QLabel(self.Training)
        self.trainingTitle = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainingTitle.sizePolicy().hasHeightForWidth())
        self.trainingTitle.setSizePolicy(sizePolicy)
        self.trainingTitle.setText(title)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        self.trainingTitle.setFont(font)
        self.trainingTitle.setObjectName("trainingTitle")
        self.trainingLayout.addWidget(self.trainingTitle, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.trainingLayout.addItem(spacerItem, 2, 0, 1, 1)
        # self.trainBtn = QtWidgets.QPushButton(self.Training)
        self.trainBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainBtn.sizePolicy().hasHeightForWidth())
        self.trainBtn.setSizePolicy(sizePolicy)
        self.trainBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.trainBtn.setStyleSheet("\n"
                                    "QPushButton#trainBtn:hover\n"
                                    "{\n"
                                    "    image: url(:/StartTrainingBtn/startTrainingHover.png);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#trainBtn:pressed\n"
                                    "{\n"
                                    "    image: url(:/StartTrainingBtn/startTrainingPush.png);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#trainBtn\n"
                                    "{\n"
                                    "    image: url(:/StartTrainingBtn/startTrainingDef.png);\n"
                                    "    background:transparent;\n"
                                    "\n"
                                    "}")
        self.trainBtn.setText("")
        self.trainBtn.setIconSize(QtCore.QSize(10, 10))
        self.trainBtn.setAutoRepeatDelay(4)
        self.trainBtn.setAutoRepeatInterval(4)
        self.trainBtn.setObjectName("trainBtn")
        self.trainingLayout.addWidget(self.trainBtn, 3, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.trainingLayout, 0, 0, 1, 1)


        self.trainingDir.textChanged.connect(partial(controller.selectionDirChanges, self.trainingDir))
        self.browseBtnTraining.clicked.connect(partial(controller.browseDirBtnClicked, self.trainingDir, "Training directory loaded successfully"))
        self.trainBtn.clicked.connect(controller.startTrainingGuide)


