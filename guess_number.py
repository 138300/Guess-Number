from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GuessNumber(object):
    def setupUi(self, GuessNumber):
        GuessNumber.setObjectName("GuessNumber")
        GuessNumber.resize(801, 451)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/countdown (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GuessNumber.setWindowIcon(icon)
        GuessNumber.setStyleSheet("background-color:#F4EEFF;")
        self.centralwidget = QtWidgets.QWidget(GuessNumber)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.welcome_page = QtWidgets.QWidget()
        self.welcome_page.setObjectName("welcome_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.welcome_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.start_btn = QtWidgets.QPushButton(self.welcome_page)
        self.start_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.start_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setStyleSheet("#start_btn{\n"
"background-color:#FFD460;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"#start_btn::hover{\n"
"background-color:white;\n"
"color:#FFD460;\n"
"}\n"
"#start_btn::pressed{\n"
"border-radius:5px;\n"
"width:20px;\n"
"}")
        self.start_btn.setObjectName("start_btn")
        self.gridLayout.addWidget(self.start_btn, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.icon = QtWidgets.QLabel(self.welcome_page)
        self.icon.setMaximumSize(QtCore.QSize(300, 150))
        self.icon.setStyleSheet("background-color:none;")
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("icons/countdown (2).png"))
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.title = QtWidgets.QLabel(self.welcome_page)
        self.title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color:#FC5185;\n"
"background-color:none")
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.welcome_page)
        self.label.setMinimumSize(QtCore.QSize(20, 0))
        self.label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FFD460;\n"
"background-color:none")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.stackedWidget.addWidget(self.welcome_page)
        self.game_page = QtWidgets.QWidget()
        self.game_page.setObjectName("game_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.game_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bigger_btn = QtWidgets.QPushButton(self.game_page)
        self.bigger_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bigger_btn.setFont(font)
        self.bigger_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bigger_btn.setStyleSheet("#bigger_btn{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"#bigger_btn::hover{\n"
"background-color:white;\n"
"color:#FF2E63;\n"
"}\n"
"#bigger_btn::pressed{\n"
"border-radius:5px;\n"
"width:20px;\n"
"}")
        self.bigger_btn.setObjectName("bigger_btn")
        self.horizontalLayout.addWidget(self.bigger_btn)
        self.correct_btn = QtWidgets.QPushButton(self.game_page)
        self.correct_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.correct_btn.setFont(font)
        self.correct_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.correct_btn.setStyleSheet("#correct_btn{\n"
"background-color:#1FAB89;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"#correct_btn::hover{\n"
"background-color:white;\n"
"color:#1FAB89;\n"
"}\n"
"#correct_btn::pressed{\n"
"border-radius:5px;\n"
"width:20px;\n"
"}")
        self.correct_btn.setObjectName("correct_btn")
        self.horizontalLayout.addWidget(self.correct_btn)
        self.smaller_btn = QtWidgets.QPushButton(self.game_page)
        self.smaller_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.smaller_btn.setFont(font)
        self.smaller_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.smaller_btn.setStyleSheet("#smaller_btn{\n"
"background-color:#FFD460;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"#smaller_btn::hover{\n"
"background-color:white;\n"
"color:#FFD460;\n"
"}\n"
"#smaller::pressed{\n"
"border-radius:5px;\n"
"width:20px;\n"
"}")
        self.smaller_btn.setObjectName("smaller_btn")
        self.horizontalLayout.addWidget(self.smaller_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_2 = QtWidgets.QLabel(self.game_page)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("background-color:none;")
        self.title_2.setObjectName("title_2")
        self.horizontalLayout_2.addWidget(self.title_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.guessed_number = QtWidgets.QLabel(self.game_page)
        self.guessed_number.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.guessed_number.setFont(font)
        self.guessed_number.setStyleSheet("background-color:white;\n"
"padding:20px 25px;\n"
"border-radius:15px;\n"
"border-color: rgb(255, 255, 0);")
        self.guessed_number.setObjectName("guessed_number")
        self.horizontalLayout_2.addWidget(self.guessed_number, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.stackedWidget.addWidget(self.game_page)
        self.finish_page = QtWidgets.QWidget()
        self.finish_page.setObjectName("finish_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.finish_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.thanks = QtWidgets.QLabel(self.finish_page)
        self.thanks.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.thanks.setFont(font)
        self.thanks.setStyleSheet("background-color:none;\n"
"color:#FF2E63;")
        self.thanks.setObjectName("thanks")
        self.gridLayout_3.addWidget(self.thanks, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.play_again_btn = QtWidgets.QPushButton(self.finish_page)
        self.play_again_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.play_again_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.play_again_btn.setFont(font)
        self.play_again_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_again_btn.setStyleSheet("#play_again_btn{\n"
"background-color:#FFD460;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"#play_again_btn::hover{\n"
"background-color:white;\n"
"color:#FFD460;\n"
"}\n"
"#play_again_btn::pressed{\n"
"border-radius:5px;\n"
"width:20px;\n"
"}")
        self.play_again_btn.setObjectName("play_again_btn")
        self.gridLayout_3.addWidget(self.play_again_btn, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.stackedWidget.addWidget(self.finish_page)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)
        GuessNumber.setCentralWidget(self.centralwidget)

        self.retranslateUi(GuessNumber)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(GuessNumber)

    def retranslateUi(self, GuessNumber):
        _translate = QtCore.QCoreApplication.translate
        GuessNumber.setWindowTitle(_translate("GuessNumber", "Guess Number"))
        self.start_btn.setText(_translate("GuessNumber", "Start"))
        self.title.setText(_translate("GuessNumber", "Welcome To Guess Number Game"))
        self.label.setText(_translate("GuessNumber", "(Choose a number and click on Start)"))
        self.bigger_btn.setText(_translate("GuessNumber", "Guessed number is bigger"))
        self.correct_btn.setText(_translate("GuessNumber", "Guessed number is correct"))
        self.smaller_btn.setText(_translate("GuessNumber", "Guussed number is smaller"))
        self.title_2.setText(_translate("GuessNumber", "Guessed Number Is:"))
        self.guessed_number.setText(_translate("GuessNumber", "0"))
        self.thanks.setText(_translate("GuessNumber", "Thanks For Playing"))
        self.play_again_btn.setText(_translate("GuessNumber", "Play Again"))



