# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab6_mwTdmrGX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(549, 597)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 551, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(510, 8, 15, 15))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_exp.setFont(font)
        self.pushButton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_exp.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-radius: 7px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 111, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 153, 0);\n"
"}")
        self.pushButton_close = QPushButton(self.frame_header)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(530, 8, 16, 16))
        self.pushButton_close.setFont(font)
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 8px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(175, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(229, 0, 0);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(119, 50, 321, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 120, 321, 371))
        self.frame.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_drop = QLabel(self.frame)
        self.label_drop.setObjectName(u"label_drop")
        self.label_drop.setGeometry(QRect(0, 120, 321, 121))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_drop.setFont(font2)
        self.label_drop.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_drop.setAlignment(Qt.AlignCenter)
        self.pushButtonNext = QPushButton(self.centralwidget)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setGeometry(QRect(200, 520, 171, 51))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButtonNext.setFont(font3)
        self.pushButtonNext.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonNext.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 31, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color:rgb(20, 22, 25)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(41, 46, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(33, 37, 42);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ECG Phase Portrait", None))
        self.label_drop.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Drop your signal</p><p>data here</p></body></html>", None))
        self.pushButtonNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

