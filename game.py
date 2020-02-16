# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyInstaller.utils.win32 import icon
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        player=""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QLineEdit(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(150, 400, 71, 51))
        self.b1.setObjectName("b1")
        self.b4 = QtWidgets.QLineEdit(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(150, 450, 71, 51))
        self.b4.setObjectName("b4")
        self.b7 = QtWidgets.QLineEdit(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(150, 500, 71, 51))
        self.b7.setObjectName("b7")
        self.b2 = QtWidgets.QLineEdit(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(220, 400, 61, 51))
        self.b2.setObjectName("b2")
        self.b5 = QtWidgets.QLineEdit(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(220, 450, 61, 51))
        self.b5.setObjectName("b5")
        self.b9 = QtWidgets.QLineEdit(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(280, 500, 61, 51))
        self.b9.setObjectName("b9")
        self.b3 = QtWidgets.QLineEdit(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(280, 400, 61, 51))
        self.b3.setObjectName("b3")
        self.b6 = QtWidgets.QLineEdit(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(280, 450, 61, 51))
        self.b6.setObjectName("b6")
        self.b8 = QtWidgets.QLineEdit(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(220, 500, 61, 51))
        self.b8.setObjectName("b8")
        self.player1name = QtWidgets.QLabel(self.centralwidget)
        self.player1name.setGeometry(QtCore.QRect(430, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.player1name.setFont(font)
        self.player1name.setObjectName("player1name")
        self.player2name = QtWidgets.QLabel(self.centralwidget)
        self.player2name.setGeometry(QtCore.QRect(430, 220, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.player2name.setFont(font)
        self.player2name.setObjectName("player2name")
        self.P1nameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.P1nameEntry.setGeometry(QtCore.QRect(620, 161, 131, 31))
        self.P1nameEntry.setObjectName("P1nameEntry")
        self.P2nameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.P2nameEntry.setGeometry(QtCore.QRect(620, 221, 131, 31))
        self.P2nameEntry.setObjectName("P2nameEntry")
        self.InfoBox = QtWidgets.QLineEdit(self.centralwidget)
        self.InfoBox.setGeometry(QtCore.QRect(30, 160, 381, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.InfoBox.setFont(font)
        self.InfoBox.setObjectName("InfoBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 410, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 410, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 410, 61, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 460, 61, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 460, 61, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 460, 61, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 510, 61, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(540, 510, 61, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(610, 510, 61, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 290, 135, 35))
        self.pushButton_10.setObjectName("pushButton_10")
        self.welcome_note = QtWidgets.QLabel(self.centralwidget)
        self.welcome_note.setGeometry(QtCore.QRect(180, 20, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.welcome_note.setFont(font)
        self.welcome_note.setObjectName("welcome_note")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def btn1(self):
        if icon=="X":
         self.b1.setText("X")
        else:
         self.b1.setText("O")

         self.InfoBox.setText("Now It's your turn {}".format(self.P2nameEntry.text()))

    def btn2(self):
        self.b2.setText("")

    def btn3(self):
        self.b3.setText("X")

    def btn4(self):
        self.b4.setText("X")

    def btn5(self):
        self.b5.setText("X")

    def btn6(self):
        self.b6.setText("X")

    def btn7(self):
        self.b7.setText("X")

    def btn8(self):
        self.b8.setText("X")

    def btn9(self):
        self.b9.setText("X")

    def start(self):
        self.InfoBox.setText("Let's Start,Make your move {}".format(self.P1nameEntry.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.player1name.setText(_translate("MainWindow", "Player 1 Name:"))
        self.player2name.setText(_translate("MainWindow", "Player 2 Name:"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton.clicked.connect(self.btn1)
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "Start"))
        self.pushButton_10.clicked.connect(self.start)
        self.welcome_note.setText(_translate("MainWindow", "Welcome to The Tic Tac Toe"))
        self.InfoBox.setText("WELCOME")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
