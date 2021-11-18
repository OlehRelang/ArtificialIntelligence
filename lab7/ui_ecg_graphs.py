# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ecg_graphsztXhXL.ui'
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
        MainWindow.resize(1560, 953)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 1561, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(1520, 8, 15, 15))
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
        self.pushButton_close.setGeometry(QRect(1540, 8, 16, 16))
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
        self.label_2.setGeometry(QRect(610, 40, 350, 41))
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
        self.EcgWidget_1 = QWidget(self.centralwidget)
        self.EcgWidget_1.setObjectName(u"EcgWidget_1")
        self.EcgWidget_1.setGeometry(QRect(20, 90, 741, 381))
        self.EcgWidget_1.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.EcgWidget_2 = QWidget(self.centralwidget)
        self.EcgWidget_2.setObjectName(u"EcgWidget_2")
        self.EcgWidget_2.setGeometry(QRect(800, 90, 741, 381))
        self.EcgWidget_2.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.EcgWidget_3 = QWidget(self.centralwidget)
        self.EcgWidget_3.setObjectName(u"EcgWidget_3")
        self.EcgWidget_3.setGeometry(QRect(20, 490, 741, 381))
        self.EcgWidget_3.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.EcgWidget_4 = QWidget(self.centralwidget)
        self.EcgWidget_4.setObjectName(u"EcgWidget_4")
        self.EcgWidget_4.setGeometry(QRect(800, 490, 741, 381))
        self.EcgWidget_4.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 90, 91, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(680, 490, 91, 41))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1460, 90, 91, 41))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1460, 490, 91, 41))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.pushButtonNext = QPushButton(self.centralwidget)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setGeometry(QRect(690, 890, 181, 51))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ECG Plots", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0415\u041a\u0413 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0415\u041a\u0413 3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0415\u041a\u0413 2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0415\u041a\u0413 4", None))
        self.pushButtonNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

