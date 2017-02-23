# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(320, 240)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color : rgb(25, 25, 25);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color : rgb(51, 51, 51);\n"
"    border : 2px;\n"
"    border-style: solid;\n"
"    border-color:rgb(25, 25, 25);\n"
"    color : rgb(230, 230, 230);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.leftButton = QtWidgets.QPushButton(self.centralWidget)
        self.leftButton.setGeometry(QtCore.QRect(5, 50, 50, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.leftButton.setFont(font)
        self.leftButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.leftButton.setStyleSheet("background-color : rgb(76, 76, 76);\n"
"border : 2px;\n"
"border-style: solid;\n"
"border-color:rgb(25, 25, 25);\n"
"")
        self.leftButton.setFlat(False)
        self.leftButton.setObjectName("leftButton")
        self.rightButton = QtWidgets.QPushButton(self.centralWidget)
        self.rightButton.setGeometry(QtCore.QRect(205, 50, 50, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.rightButton.setFont(font)
        self.rightButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.rightButton.setStyleSheet("background-color : rgb(76, 76, 76);\n"
"border : 2px;\n"
"border-style: solid;\n"
"border-color:rgb(25, 25, 25);\n"
"")
        self.rightButton.setFlat(False)
        self.rightButton.setObjectName("rightButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(55, 50, 150, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lcdNumber.setStyleSheet("background-color : rgb(76, 76, 76);\n"
"border : 2px;\n"
"border-style: solid;\n"
"border-color:rgb(25, 25, 25);\n"
"color : rgb(230, 230, 230);\n"
"")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 123456.0)
        self.lcdNumber.setProperty("intValue", 123456)
        self.lcdNumber.setObjectName("lcdNumber")
        self.push01Button = QtWidgets.QPushButton(self.centralWidget)
        self.push01Button.setGeometry(QtCore.QRect(5, 110, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push01Button.setFont(font)
        self.push01Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push01Button.setStyleSheet("")
        self.push01Button.setFlat(False)
        self.push01Button.setObjectName("push01Button")
        self.push02Button = QtWidgets.QPushButton(self.centralWidget)
        self.push02Button.setGeometry(QtCore.QRect(55, 110, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push02Button.setFont(font)
        self.push02Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push02Button.setObjectName("push02Button")
        self.push03Button = QtWidgets.QPushButton(self.centralWidget)
        self.push03Button.setGeometry(QtCore.QRect(105, 110, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push03Button.setFont(font)
        self.push03Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push03Button.setObjectName("push03Button")
        self.push04Button = QtWidgets.QPushButton(self.centralWidget)
        self.push04Button.setGeometry(QtCore.QRect(5, 150, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push04Button.setFont(font)
        self.push04Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push04Button.setObjectName("push04Button")
        self.push05Button = QtWidgets.QPushButton(self.centralWidget)
        self.push05Button.setGeometry(QtCore.QRect(55, 150, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push05Button.setFont(font)
        self.push05Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push05Button.setObjectName("push05Button")
        self.push06Button = QtWidgets.QPushButton(self.centralWidget)
        self.push06Button.setGeometry(QtCore.QRect(105, 150, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push06Button.setFont(font)
        self.push06Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push06Button.setObjectName("push06Button")
        self.push08Button = QtWidgets.QPushButton(self.centralWidget)
        self.push08Button.setGeometry(QtCore.QRect(55, 190, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push08Button.setFont(font)
        self.push08Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push08Button.setObjectName("push08Button")
        self.push09Button = QtWidgets.QPushButton(self.centralWidget)
        self.push09Button.setGeometry(QtCore.QRect(105, 190, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push09Button.setFont(font)
        self.push09Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push09Button.setObjectName("push09Button")
        self.push07Button = QtWidgets.QPushButton(self.centralWidget)
        self.push07Button.setGeometry(QtCore.QRect(5, 190, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push07Button.setFont(font)
        self.push07Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push07Button.setObjectName("push07Button")
        self.push00Button = QtWidgets.QPushButton(self.centralWidget)
        self.push00Button.setGeometry(QtCore.QRect(155, 190, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.push00Button.setFont(font)
        self.push00Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.push00Button.setObjectName("push00Button")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(255, 50, 60, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.playButton.setStyleSheet("QPushButton#playButton{\n"
"    background-color : rgb(255, 204, 102);\n"
"    color : rgb(51, 51, 51);\n"
"}")
        self.playButton.setObjectName("playButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(205, 150, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_1.setStyleSheet("background-color : rgb(76, 76, 76);\n"
"border : 2px;\n"
"border-style: solid;\n"
"border-color:rgb(25, 25, 25);\n"
"")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.songLabel = QtWidgets.QLabel(self.centralWidget)
        self.songLabel.setEnabled(True)
        self.songLabel.setGeometry(QtCore.QRect(0, 0, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.songLabel.setFont(font)
        self.songLabel.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.songLabel.setToolTip("")
        self.songLabel.setStatusTip("")
        self.songLabel.setStyleSheet("QLabel{\n"
"    color : rgb(230, 230, 230);\n"
"    border : 2px;\n"
"    border-style: solid;\n"
"    border-color:rgb(25, 25, 25);\n"
"}")
        self.songLabel.setObjectName("songLabel")
        self.quitButton = QtWidgets.QPushButton(self.centralWidget)
        self.quitButton.setGeometry(QtCore.QRect(255, 190, 60, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quitButton.setFont(font)
        self.quitButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.quitButton.setStyleSheet("QPushButton#quitButton{\n"
"    background-color : rgb(255, 102, 102);\n"
"    color : rgb(230, 230, 230);\n"
"}")
        self.quitButton.setObjectName("quitButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(205, 110, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_2.setStyleSheet("background-color : rgb(76, 76, 76);\n"
"border : 2px;\n"
"border-style: solid;\n"
"border-color:rgb(25, 25, 25);\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.delButton = QtWidgets.QPushButton(self.centralWidget)
        self.delButton.setGeometry(QtCore.QRect(155, 110, 50, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.delButton.setFont(font)
        self.delButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.delButton.setObjectName("delButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(205, 190, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_3.setStyleSheet("background-color : rgb(76, 76, 76);\n"
"border : 2px;\n"
"border-style: solid;\n"
"border-color:rgb(25, 25, 25);\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.loopButton = QtWidgets.QPushButton(self.centralWidget)
        self.loopButton.setGeometry(QtCore.QRect(255, 150, 60, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loopButton.setFont(font)
        self.loopButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.loopButton.setStyleSheet("QPushButton#loopButton{\n"
"    background-color : rgb(0, 128, 128);\n"
"    color : rgb(230, 230, 230);\n"
"}")
        self.loopButton.setObjectName("loopButton")
        self.albumButton = QtWidgets.QPushButton(self.centralWidget)
        self.albumButton.setGeometry(QtCore.QRect(255, 110, 60, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.albumButton.setFont(font)
        self.albumButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.albumButton.setStyleSheet("QPushButton#albumButton{\n"
"    background-color : rgb(64, 128, 0);\n"
"    color : rgb(230, 230, 230);\n"
"}")
        self.albumButton.setObjectName("albumButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.leftButton.setText(_translate("MainWindow", "<"))
        self.rightButton.setText(_translate("MainWindow", ">"))
        self.push01Button.setText(_translate("MainWindow", "1"))
        self.push02Button.setText(_translate("MainWindow", "2"))
        self.push03Button.setText(_translate("MainWindow", "3"))
        self.push04Button.setText(_translate("MainWindow", "4"))
        self.push05Button.setText(_translate("MainWindow", "5"))
        self.push06Button.setText(_translate("MainWindow", "6"))
        self.push08Button.setText(_translate("MainWindow", "8"))
        self.push09Button.setText(_translate("MainWindow", "9"))
        self.push07Button.setText(_translate("MainWindow", "7"))
        self.push00Button.setText(_translate("MainWindow", "0"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.songLabel.setText(_translate("MainWindow", "Breizh JukeBox 1.0"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.delButton.setText(_translate("MainWindow", "Del"))
        self.loopButton.setText(_translate("MainWindow", "Shuffle"))
        self.albumButton.setText(_translate("MainWindow", "Album"))

