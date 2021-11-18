# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ecg_portraitsLIvjal.ui'
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


class Ui_PortraitMainWindow(object):
    def setupUi(self, PortraitMainWindow):
        if PortraitMainWindow.objectName():
            PortraitMainWindow.setObjectName(u"PortraitMainWindow")
        PortraitMainWindow.resize(1192, 788)
        PortraitMainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(PortraitMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 1191, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(1150, 8, 15, 15))
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
        self.pushButton_close.setGeometry(QRect(1170, 8, 16, 16))
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
        self.label_2.setGeometry(QRect(420, 40, 351, 41))
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
        self.EcgWidget = QWidget(self.centralwidget)
        self.EcgWidget.setObjectName(u"EcgWidget")
        self.EcgWidget.setGeometry(QRect(380, 100, 781, 511))
        self.EcgWidget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(40, 230, 311, 291))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.tableView.setFont(font2)
        self.tableView.setLayoutDirection(Qt.LeftToRight)
        self.tableView.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border:none;\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"text-align: center;")
        self.tableView.setFrameShape(QFrame.StyledPanel)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setTextElideMode(Qt.ElideMiddle)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(25)
        self.tableView.horizontalHeader().setDefaultSectionSize(78)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setMinimumSectionSize(10)
        self.tableView.verticalHeader().setDefaultSectionSize(73)
        self.pushButtonFind = QPushButton(self.centralwidget)
        self.pushButtonFind.setObjectName(u"pushButtonFind")
        self.pushButtonFind.setGeometry(QRect(490, 690, 171, 51))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButtonFind.setFont(font3)
        self.pushButtonFind.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonFind.setStyleSheet(u"QPushButton {\n"
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
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 130, 311, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButtonCalc = QPushButton(self.centralwidget)
        self.pushButtonCalc.setObjectName(u"pushButtonCalc")
        self.pushButtonCalc.setGeometry(QRect(100, 540, 181, 51))
        self.pushButtonCalc.setFont(font3)
        self.pushButtonCalc.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonCalc.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 180, 311, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 230, 41, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        PortraitMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PortraitMainWindow)

        QMetaObject.connectSlotsByName(PortraitMainWindow)
    # setupUi

    def retranslateUi(self, PortraitMainWindow):
        PortraitMainWindow.setWindowTitle(QCoreApplication.translate("PortraitMainWindow", u"MainWindow", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_2.setText(QCoreApplication.translate("PortraitMainWindow", u"ECG Phase Portraits", None))
        self.pushButtonFind.setText(QCoreApplication.translate("PortraitMainWindow", u"Find", None))
        self.label_3.setText(QCoreApplication.translate("PortraitMainWindow", u"Hausdorff Matrix", None))
        self.pushButtonCalc.setText(QCoreApplication.translate("PortraitMainWindow", u"Calculate", None))
        self.label_5.setText(QCoreApplication.translate("PortraitMainWindow", u"R1", None))
        self.label_7.setText(QCoreApplication.translate("PortraitMainWindow", u"R2", None))
        self.label_6.setText(QCoreApplication.translate("PortraitMainWindow", u"R3", None))
        self.label_4.setText(QCoreApplication.translate("PortraitMainWindow", u"R4", None))
        self.label_11.setText(QCoreApplication.translate("PortraitMainWindow", u"R1", None))
        self.label_10.setText(QCoreApplication.translate("PortraitMainWindow", u"R2", None))
        self.label_8.setText(QCoreApplication.translate("PortraitMainWindow", u"R3", None))
        self.label_9.setText(QCoreApplication.translate("PortraitMainWindow", u"R4", None))
    # retranslateUi

