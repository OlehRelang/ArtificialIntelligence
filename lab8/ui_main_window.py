# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windownTtXlA.ui'
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
        MainWindow.resize(1372, 790)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 1371, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.pushButtonExp = QPushButton(self.frame_header)
        self.pushButtonExp.setObjectName(u"pushButtonExp")
        self.pushButtonExp.setGeometry(QRect(1330, 8, 15, 15))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonExp.setFont(font)
        self.pushButtonExp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonExp.setStyleSheet(u"QPushButton{\n"
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
        self.pushButtonClose = QPushButton(self.frame_header)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setGeometry(QRect(1350, 8, 16, 16))
        self.pushButtonClose.setFont(font)
        self.pushButtonClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonClose.setStyleSheet(u"QPushButton{\n"
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 40, 1321, 661))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.RhythmoWidget_1 = QWidget(self.page)
        self.RhythmoWidget_1.setObjectName(u"RhythmoWidget_1")
        self.RhythmoWidget_1.setGeometry(QRect(20, 80, 1301, 500))
        self.RhythmoWidget_1.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 20, 351, 41))
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
        self.pushButtonTo2 = QPushButton(self.page)
        self.pushButtonTo2.setObjectName(u"pushButtonTo2")
        self.pushButtonTo2.setGeometry(QRect(570, 600, 211, 51))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButtonTo2.setFont(font2)
        self.pushButtonTo2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonTo2.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 20, 351, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButtonTo1 = QPushButton(self.page_2)
        self.pushButtonTo1.setObjectName(u"pushButtonTo1")
        self.pushButtonTo1.setGeometry(QRect(570, 600, 211, 51))
        self.pushButtonTo1.setFont(font2)
        self.pushButtonTo1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonTo1.setStyleSheet(u"QPushButton {\n"
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
        self.RhythmoWidget_2 = QWidget(self.page_2)
        self.RhythmoWidget_2.setObjectName(u"RhythmoWidget_2")
        self.RhythmoWidget_2.setGeometry(QRect(20, 80, 1301, 500))
        self.RhythmoWidget_2.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButtonStat = QPushButton(self.centralwidget)
        self.pushButtonStat.setObjectName(u"pushButtonStat")
        self.pushButtonStat.setGeometry(QRect(610, 720, 171, 51))
        self.pushButtonStat.setFont(font2)
        self.pushButtonStat.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonStat.setStyleSheet(u"QPushButton {\n"
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonExp.setText("")
        self.pushButtonClose.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rhythmogram 1", None))
        self.pushButtonTo2.setText(QCoreApplication.translate("MainWindow", u"Rhythmogram 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rhythmogram 2", None))
        self.pushButtonTo1.setText(QCoreApplication.translate("MainWindow", u"Rhythmogram 1", None))
        self.pushButtonStat.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
    # retranslateUi

