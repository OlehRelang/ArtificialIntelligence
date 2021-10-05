# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab1nLMwPJ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 598)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 635, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 6, 148, 20))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color:rgb(160, 160, 160)")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(586, 8, 15, 15))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton_exp.setFont(font1)
        self.pushButton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_exp.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(0, 170, 0);\n"
"  border-radius: 7px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 111, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: rgb(0, 153, 0);\n"
"}")
        self.pushButton_close = QPushButton(self.frame_header)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(610, 8, 16, 16))
        self.pushButton_close.setFont(font1)
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(255, 0, 0);\n"
"  border-radius: 8px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: rgb(175, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: rgb(229, 0, 0);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 40, 271, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 90, 371, 401))
        self.widget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius:20px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 341, 321))
        font3 = QFont()
        font3.setPointSize(75)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 290, 301, 91))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 180, 121, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.labelPoints = QLabel(self.centralwidget)
        self.labelPoints.setObjectName(u"labelPoints")
        self.labelPoints.setGeometry(QRect(540, 220, 61, 61))
        self.labelPoints.setFont(font2)
        self.labelPoints.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(27, 30, 34);\n"
"border-radius:15px;")
        self.labelPoints.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 290, 61, 31))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 0, 0);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(175, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(237, 0, 0);\n"
"}")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 520, 371, 41))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.lineEdit.setFont(font5)
        self.lineEdit.setStyleSheet(u"border:none;\n"
"background-color: rgb(26, 29, 32);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.pushButtonSemd = QPushButton(self.centralwidget)
        self.pushButtonSemd.setObjectName(u"pushButtonSemd")
        self.pushButtonSemd.setGeometry(QRect(460, 525, 31, 31))
        font6 = QFont()
        font6.setFamily(u"Bodoni MT Black")
        font6.setPointSize(15)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButtonSemd.setFont(font6)
        self.pushButtonSemd.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonSemd.setStyleSheet(u"QPushButton {\n"
"  background-color: #5F15A9;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(68, 14, 121);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AI Lab1", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Intelligent BOT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\U0001F916", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Points", None))
        self.labelPoints.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type your text here", None))
        self.pushButtonSemd.setText(QCoreApplication.translate("MainWindow", u"\u27a4", None))

    # retranslateUi

