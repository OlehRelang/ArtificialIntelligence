# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab6KfWjYp.ui'
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
        MainWindow.resize(1271, 969)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 1281, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(1230, 8, 15, 15))
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
        self.pushButton_close.setGeometry(QRect(1250, 8, 16, 16))
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
        self.label_2.setGeometry(QRect(490, 40, 350, 41))
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 90, 1251, 871))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.DataDropFrame = QFrame(self.page)
        self.DataDropFrame.setObjectName(u"DataDropFrame")
        self.DataDropFrame.setGeometry(QRect(480, 70, 351, 591))
        self.DataDropFrame.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.DataDropFrame.setFrameShape(QFrame.StyledPanel)
        self.DataDropFrame.setFrameShadow(QFrame.Raised)
        self.label_drop = QLabel(self.DataDropFrame)
        self.label_drop.setObjectName(u"label_drop")
        self.label_drop.setGeometry(QRect(0, 230, 351, 121))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_drop.setFont(font2)
        self.label_drop.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_drop.setAlignment(Qt.AlignCenter)
        self.pushButtonNext = QPushButton(self.page)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setGeometry(QRect(570, 750, 171, 51))
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
        self.stackedWidget.addWidget(self.page)
        self.pushButtonNext.raise_()
        self.DataDropFrame.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.EcgWidget = QWidget(self.page_2)
        self.EcgWidget.setObjectName(u"EcgWidget")
        self.EcgWidget.setGeometry(QRect(70, 20, 1111, 241))
        self.EcgWidget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.PP1Widget = QWidget(self.page_2)
        self.PP1Widget.setObjectName(u"PP1Widget")
        self.PP1Widget.setGeometry(QRect(70, 280, 1111, 241))
        self.PP1Widget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.PP2Widget = QWidget(self.page_2)
        self.PP2Widget.setObjectName(u"PP2Widget")
        self.PP2Widget.setGeometry(QRect(70, 540, 1111, 241))
        self.PP2Widget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.frame_params = QFrame(self.page_2)
        self.frame_params.setObjectName(u"frame_params")
        self.frame_params.setGeometry(QRect(280, 800, 711, 61))
        self.frame_params.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.frame_params.setFrameShape(QFrame.StyledPanel)
        self.frame_params.setFrameShadow(QFrame.Raised)
        self.TauHorizontalSlider = QSlider(self.frame_params)
        self.TauHorizontalSlider.setObjectName(u"TauHorizontalSlider")
        self.TauHorizontalSlider.setGeometry(QRect(120, 36, 481, 22))
        self.TauHorizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.79, x2:0.909, y2:0.784091, stop:0 rgba(103, 111, 122, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    margin: 2px 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.TauHorizontalSlider.setMinimum(0)
        self.TauHorizontalSlider.setMaximum(100)
        self.TauHorizontalSlider.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.frame_params)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 0, 181, 41))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(19)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_tau = QLabel(self.frame_params)
        self.label_tau.setObjectName(u"label_tau")
        self.label_tau.setGeometry(QRect(380, 0, 91, 41))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_tau.setFont(font5)
        self.label_tau.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.label_tau.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1090, 20, 91, 41))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1090, 280, 91, 41))
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1090, 540, 91, 41))
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ECG Phase Portrait", None))
        self.label_drop.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Drop your signal</p><p>data here</p></body></html>", None))
        self.pushButtonNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u03c4 =", None))
        self.label_tau.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0415\u041a\u0413", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0424\u041f 1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u041f 2", None))
    # retranslateUi

