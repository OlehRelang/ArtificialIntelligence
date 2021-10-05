# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab2tDNSDt.ui'
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
        MainWindow.resize(1050, 765)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 1051, 31))
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
        self.pushButton_exp.setGeometry(QRect(1006, 8, 15, 15))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton_exp.setFont(font1)
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
        self.pushButton_close.setGeometry(QRect(1030, 8, 16, 16))
        self.pushButton_close.setFont(font1)
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
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 40, 541, 81))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 260, 761, 401))
        self.widget.setStyleSheet(u"background-image: url(E:/Python Projects/ArtificialIntelligence/lab2/bg.jpg);\n"
"border-radius:20px;")
        self.label_sign = QLabel(self.widget)
        self.label_sign.setObjectName(u"label_sign")
        self.label_sign.setGeometry(QRect(350, 170, 71, 61))
        self.label_sign.setFont(font2)
        self.label_sign.setStyleSheet(u"background: transparent;\n"
"color: rgb(87, 21, 191)")
        self.label_sign.setAlignment(Qt.AlignCenter)
        self.label_date = QLabel(self.widget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(231, 0, 321, 41))
        self.label_date.setFont(font2)
        self.label_date.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_date.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_text = QLabel(self.widget)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setGeometry(QRect(10, 70, 271, 271))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_text.setFont(font3)
        self.label_text.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_sign_name = QLabel(self.widget)
        self.label_sign_name.setObjectName(u"label_sign_name")
        self.label_sign_name.setGeometry(QRect(20, 20, 191, 51))
        self.label_sign_name.setFont(font2)
        self.label_sign_name.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_sign_name.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_text_2 = QLabel(self.widget)
        self.label_text_2.setObjectName(u"label_text_2")
        self.label_text_2.setGeometry(QRect(480, 70, 271, 271))
        self.label_text_2.setFont(font3)
        self.label_text_2.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_text_2.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_date.raise_()
        self.label_sign.raise_()
        self.label_text.raise_()
        self.label_sign_name.raise_()
        self.label_text_2.raise_()
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(170, 670, 731, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton2_2 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton2_2.setObjectName(u"pushButton2_2")
        self.pushButton2_2.setMaximumSize(QSize(161, 41))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton2_2.setFont(font4)
        self.pushButton2_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton2_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton2_2)

        self.pushButton2_3 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton2_3.setObjectName(u"pushButton2_3")
        self.pushButton2_3.setMaximumSize(QSize(161, 41))
        self.pushButton2_3.setFont(font4)
        self.pushButton2_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton2_3.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton2_3)

        self.pushButton2_4 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton2_4.setObjectName(u"pushButton2_4")
        self.pushButton2_4.setMaximumSize(QSize(161, 41))
        self.pushButton2_4.setFont(font4)
        self.pushButton2_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton2_4.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton2_4)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 120, 1021, 131))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayoutWidget = QWidget(self.page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-10, 50, 1011, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton1 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setMaximumSize(QSize(51, 51))
        font5 = QFont()
        font5.setFamily(u"Bodoni MT Black")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton1.setFont(font5)
        self.pushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton1.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setMaximumSize(QSize(51, 51))
        self.pushButton2.setFont(font5)
        self.pushButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton2.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setMaximumSize(QSize(51, 51))
        self.pushButton3.setFont(font5)
        self.pushButton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton3.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton3)

        self.pushButton4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setMaximumSize(QSize(51, 51))
        self.pushButton4.setFont(font5)
        self.pushButton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton4.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton4)

        self.pushButton5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton5.setObjectName(u"pushButton5")
        self.pushButton5.setMaximumSize(QSize(51, 51))
        self.pushButton5.setFont(font5)
        self.pushButton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton5.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton5)

        self.pushButton6 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton6.setObjectName(u"pushButton6")
        self.pushButton6.setMaximumSize(QSize(51, 51))
        self.pushButton6.setFont(font5)
        self.pushButton6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton6.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton6)

        self.pushButton7 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton7.setObjectName(u"pushButton7")
        self.pushButton7.setMaximumSize(QSize(51, 51))
        self.pushButton7.setFont(font5)
        self.pushButton7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton7.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton7)

        self.pushButton8 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton8.setObjectName(u"pushButton8")
        self.pushButton8.setMaximumSize(QSize(51, 51))
        self.pushButton8.setFont(font5)
        self.pushButton8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton8.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton8)

        self.pushButton9 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton9.setObjectName(u"pushButton9")
        self.pushButton9.setMaximumSize(QSize(51, 51))
        self.pushButton9.setFont(font5)
        self.pushButton9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton9.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton9)

        self.pushButton10 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton10.setObjectName(u"pushButton10")
        self.pushButton10.setMaximumSize(QSize(51, 51))
        self.pushButton10.setFont(font5)
        self.pushButton10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton10.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton10)

        self.pushButton11 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton11.setObjectName(u"pushButton11")
        self.pushButton11.setMaximumSize(QSize(51, 51))
        self.pushButton11.setFont(font5)
        self.pushButton11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton11.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton11)

        self.pushButton12 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton12.setObjectName(u"pushButton12")
        self.pushButton12.setMaximumSize(QSize(51, 51))
        self.pushButton12.setFont(font5)
        self.pushButton12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton12.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton12)

        self.horizontalLayoutWidget_2 = QWidget(self.page)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 10, 1011, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(111, 31))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(111, 31))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(111, 31))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(111, 31))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_10)

        self.label_12 = QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(111, 31))
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_12)

        self.label_14 = QLabel(self.horizontalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(111, 31))
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_14)

        self.label_17 = QLabel(self.horizontalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(111, 31))
        self.label_17.setFont(font6)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.label_16 = QLabel(self.horizontalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(111, 31))
        self.label_16.setFont(font6)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_16)

        self.label_15 = QLabel(self.horizontalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(111, 31))
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.label_13 = QLabel(self.horizontalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(111, 31))
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_13)

        self.label_11 = QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(111, 31))
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(111, 31))
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(330, 50, 371, 41))
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"border: none;\n"
"border-radius: 15px;\n"
"background-color: rgb(28, 31, 35);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.pushButtonSend = QPushButton(self.page_2)
        self.pushButtonSend.setObjectName(u"pushButtonSend")
        self.pushButtonSend.setGeometry(QRect(660, 62, 31, 21))
        font7 = QFont()
        font7.setFamily(u"Bodoni MT Black")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.pushButtonSend.setFont(font7)
        self.pushButtonSend.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonSend.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(950, 260, 51, 23))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 260, 51, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AI Lab2", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Horoscope", None))
        self.label_sign.setText("")
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_sign_name.setText("")
        self.label_text_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton2_2.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.pushButton2_3.setText(QCoreApplication.translate("MainWindow", u"For a week", None))
        self.pushButton2_4.setText(QCoreApplication.translate("MainWindow", u"For a month", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"\u2652", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"\u2653", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"\u2648", None))
        self.pushButton4.setText(QCoreApplication.translate("MainWindow", u"\u2649", None))
        self.pushButton5.setText(QCoreApplication.translate("MainWindow", u"\u264a", None))
        self.pushButton6.setText(QCoreApplication.translate("MainWindow", u"\u264b", None))
        self.pushButton7.setText(QCoreApplication.translate("MainWindow", u"\u264c", None))
        self.pushButton8.setText(QCoreApplication.translate("MainWindow", u"\u264d", None))
        self.pushButton9.setText(QCoreApplication.translate("MainWindow", u"\u264e", None))
        self.pushButton10.setText(QCoreApplication.translate("MainWindow", u"\u264f", None))
        self.pushButton11.setText(QCoreApplication.translate("MainWindow", u"\u2650", None))
        self.pushButton12.setText(QCoreApplication.translate("MainWindow", u"\u2651", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Aquarius", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"The Fish", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"The Ram", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"The Bull", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"The Twins", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Cancer", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"The Lion", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Virgo", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"The Scales", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Scorpio", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"The Archer", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Goat-Corned", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter birthdate (DD.MM.YYYY)", None))
        self.pushButtonSend.setText(QCoreApplication.translate("MainWindow", u"\u27a4", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"<-", None))
    # retranslateUi

