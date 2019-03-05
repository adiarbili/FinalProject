from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class TestingView(QtWidgets.QWidget):

    def __init__(self, title, controller):
        super().__init__()
        self.setObjectName("Testing")
        self.gridLayout_3 = QtWidgets.QGridLayout(self)

        # self.Testing = QtWidgets.QWidget()
        # self.Testing.setObjectName("Testing")
        # self.gridLayout_3 = QtWidgets.QGridLayout(self.Testing)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TestingLayout = QtWidgets.QGridLayout()
        self.TestingLayout.setSpacing(0)
        self.TestingLayout.setObjectName("TestingLayout")
        # self.testingTitle = QtWidgets.QLabel(self.Testing)
        self.testingTitle = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testingTitle.sizePolicy().hasHeightForWidth())
        self.testingTitle.setSizePolicy(sizePolicy)
        self.testingTitle.setText(title)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        self.testingTitle.setFont(font)
        self.testingTitle.setObjectName("testingTitle")
        self.TestingLayout.addWidget(self.testingTitle, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.ImageDirLayout2 = QtWidgets.QHBoxLayout()
        self.ImageDirLayout2.setContentsMargins(20, 0, -1, 0)
        self.ImageDirLayout2.setSpacing(0)
        self.ImageDirLayout2.setObjectName("ImageDirLayout2")
        # self.chosenImg = QtWidgets.QLabel(self.Testing)
        self.chosenImg = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chosenImg.sizePolicy().hasHeightForWidth())
        self.chosenImg.setSizePolicy(sizePolicy)
        self.chosenImg.setMinimumSize(QtCore.QSize(210, 210))
        self.chosenImg.setStyleSheet("QLabel#chosenImg\n"
                                     "{\n"
                                     "border-image: url(:/DefaultImage/defualtImage.png);\n"
                                     "\n"
                                     "}")
        self.chosenImg.setText("")
        self.chosenImg.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.chosenImg.setObjectName("chosenImg")
        self.ImageDirLayout2.addWidget(self.chosenImg)
        # self.testBtn = QtWidgets.QPushButton(self.Testing)
        self.testBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testBtn.sizePolicy().hasHeightForWidth())
        self.testBtn.setSizePolicy(sizePolicy)
        self.testBtn.setMinimumSize(QtCore.QSize(85, 40))
        self.testBtn.setStyleSheet("\n"
                                   "QPushButton#testBtn:hover\n"
                                   "{\n"
                                   "    \n"
                                   "    image: url(:/TestBtn/testHover.png);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#testBtn:pressed\n"
                                   "{\n"
                                   "    \n"
                                   "    image: url(:/TestBtn/testPush.png);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#testBtn\n"
                                   "{\n"
                                   "    \n"
                                   "    image: url(:/TestBtn/testDef.png);\n"
                                   "    background:transparent;\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "")
        self.testBtn.setText("")
        self.testBtn.setIconSize(QtCore.QSize(10, 10))
        self.testBtn.setAutoRepeatDelay(4)
        self.testBtn.setAutoRepeatInterval(4)
        self.testBtn.setObjectName("testBtn")
        self.ImageDirLayout2.addWidget(self.testBtn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.TestingLayout.addLayout(self.ImageDirLayout2, 4, 0, 1, 2)
        self.ImageDirLayout = QtWidgets.QVBoxLayout()
        self.ImageDirLayout.setContentsMargins(-1, 20, -1, -1)
        self.ImageDirLayout.setObjectName("ImageDirLayout")
        # self.browseBoxTesting_2 = QtWidgets.QGroupBox(self.Testing)
        self.browseBoxTesting_2 = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBoxTesting_2.sizePolicy().hasHeightForWidth())
        self.browseBoxTesting_2.setSizePolicy(sizePolicy)
        self.browseBoxTesting_2.setMinimumSize(QtCore.QSize(0, 60))
        self.browseBoxTesting_2.setStyleSheet("border-style: none")
        self.browseBoxTesting_2.setTitle("")
        self.browseBoxTesting_2.setFlat(False)
        self.browseBoxTesting_2.setCheckable(False)
        self.browseBoxTesting_2.setObjectName("browseBoxTesting_2")
        self.browseBtnModel = QtWidgets.QPushButton(self.browseBoxTesting_2)
        self.browseBtnModel.setGeometry(QtCore.QRect(319, 6, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnModel.sizePolicy().hasHeightForWidth())
        self.browseBtnModel.setSizePolicy(sizePolicy)
        self.browseBtnModel.setStyleSheet("QPushButton#browseBtnModel:hover\n"
                                          "{\n"
                                          "    image: url(:/BrowseBtn/browseHover.png);\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#browseBtnModel:pressed\n"
                                          "{\n"
                                          "    image: url(:/BrowseBtn/browsePush.png);\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#browseBtnModel\n"
                                          "{\n"
                                          "    image: url(:/BrowseBtn/browseDef.png);\n"
                                          "    background:transparent;\n"
                                          "\n"
                                          "}")
        self.browseBtnModel.setText("")
        self.browseBtnModel.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnModel.setAutoRepeatDelay(4)
        self.browseBtnModel.setAutoRepeatInterval(4)
        self.browseBtnModel.setObjectName("browseBtnModel")
        self.customizeTextboxModelTesting = QtWidgets.QLabel(self.browseBoxTesting_2)
        self.customizeTextboxModelTesting.setGeometry(QtCore.QRect(4, 10, 309, 43))
        self.customizeTextboxModelTesting.setText("")
        self.customizeTextboxModelTesting.setObjectName("customizeTextboxModelTesting")
        self.customizeTextboxModelTesting.setProperty("class", "dir")
        self.modelDir = QtWidgets.QLineEdit(self.browseBoxTesting_2)
        self.modelDir.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.modelDir.setFont(font)
        self.modelDir.setAutoFillBackground(False)
        self.modelDir.setStyleSheet("")
        self.modelDir.setText("")
        self.modelDir.setPlaceholderText("Model directory")
        self.modelDir.setFrame(False)
        self.modelDir.setObjectName("modelDir")
        self.ImageDirLayout.addWidget(self.browseBoxTesting_2)
        # self.browseBoxTesting_1 = QtWidgets.QGroupBox(self.Testing)
        self.browseBoxTesting_1 = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBoxTesting_1.sizePolicy().hasHeightForWidth())
        self.browseBoxTesting_1.setSizePolicy(sizePolicy)
        self.browseBoxTesting_1.setMinimumSize(QtCore.QSize(440, 60))
        self.browseBoxTesting_1.setStyleSheet("border-style: none;\n"
                                              "")
        self.browseBoxTesting_1.setTitle("")
        self.browseBoxTesting_1.setFlat(False)
        self.browseBoxTesting_1.setCheckable(False)
        self.browseBoxTesting_1.setObjectName("browseBoxTesting_1")
        self.browseBtnImgTesting = QtWidgets.QPushButton(self.browseBoxTesting_1)
        self.browseBtnImgTesting.setGeometry(QtCore.QRect(319, 6, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseBtnImgTesting.sizePolicy().hasHeightForWidth())
        self.browseBtnImgTesting.setSizePolicy(sizePolicy)
        self.browseBtnImgTesting.setStyleSheet("QPushButton#browseBtnImgTesting:hover\n"
                                               "{\n"
                                               "    image: url(:/BrowseBtn/browseHover.png);\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#browseBtnImgTesting:pressed\n"
                                               "{\n"
                                               "    image: url(:/BrowseBtn/browsePush.png);\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#browseBtnImgTesting\n"
                                               "{\n"
                                               "    image: url(:/BrowseBtn/browseDef.png);\n"
                                               "    background:transparent;\n"
                                               "\n"
                                               "}")
        self.browseBtnImgTesting.setText("")
        self.browseBtnImgTesting.setIconSize(QtCore.QSize(10, 10))
        self.browseBtnImgTesting.setAutoRepeatDelay(4)
        self.browseBtnImgTesting.setAutoRepeatInterval(4)
        self.browseBtnImgTesting.setObjectName("browseBtnImgTesting")
        self.customizeTextboxImgTesting = QtWidgets.QLabel(self.browseBoxTesting_1)
        self.customizeTextboxImgTesting.setGeometry(QtCore.QRect(4, 10, 309, 43))
        self.customizeTextboxImgTesting.setText("")
        self.customizeTextboxImgTesting.setObjectName("customizeTextboxImgTesting")
        self.customizeTextboxImgTesting.setProperty("class", "dir")
        self.imgDir = QtWidgets.QLineEdit(self.browseBoxTesting_1)
        self.imgDir.setGeometry(QtCore.QRect(17, 16, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.imgDir.setFont(font)
        self.imgDir.setAutoFillBackground(False)
        self.imgDir.setStyleSheet("")
        self.imgDir.setText("")
        self.imgDir.setPlaceholderText("Image directory")
        self.imgDir.setFrame(False)
        self.imgDir.setObjectName("imgDir")
        self.ImageDirLayout.addWidget(self.browseBoxTesting_1)
        self.TestingLayout.addLayout(self.ImageDirLayout, 1, 0, 1, 2)
        self.gridLayout_3.addLayout(self.TestingLayout, 0, 0, 1, 1)

        # Connect events to model section.
        self.modelDir.textChanged.connect(partial(controller.selectionDirChanges, self.modelDir))
        self.browseBtnModel.clicked.connect(
            partial(controller.browseDirBtnClicked, self.modelDir, "Model directory loaded successfully"))

        # Connect events to image section.
        self.imgDir.textChanged.connect(controller.imgDirChanges)
        self.browseBtnImgTesting.clicked.connect(controller.browseImageBtnClicked)

        # Start testing process.
        self.testBtn.clicked.connect(controller.startTestingGuide)
