# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats_windowkXWvwW.ui'
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


class Ui_StatsWindow(object):
    def setupUi(self, StatsWindow):
        if StatsWindow.objectName():
            StatsWindow.setObjectName(u"StatsWindow")
        StatsWindow.resize(1372, 843)
        StatsWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(StatsWindow)
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
        self.ScatterWidget = QWidget(self.centralwidget)
        self.ScatterWidget.setObjectName(u"ScatterWidget")
        self.ScatterWidget.setGeometry(QRect(30, 160, 641, 500))
        self.ScatterWidget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.HistWidget = QWidget(self.centralwidget)
        self.HistWidget.setObjectName(u"HistWidget")
        self.HistWidget.setGeometry(QRect(700, 160, 641, 500))
        self.HistWidget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(180, 730, 1011, 81))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.tableView.setFont(font1)
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
        self.tableView.horizontalHeader().setDefaultSectionSize(145)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setMinimumSectionSize(10)
        self.tableView.verticalHeader().setDefaultSectionSize(80)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(520, 50, 331, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 110, 331, 41))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 110, 331, 41))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(180, 670, 1011, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_12)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_11)

        StatsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StatsWindow)

        QMetaObject.connectSlotsByName(StatsWindow)
    # setupUi

    def retranslateUi(self, StatsWindow):
        StatsWindow.setWindowTitle(QCoreApplication.translate("StatsWindow", u"MainWindow", None))
        self.pushButtonExp.setText("")
        self.pushButtonClose.setText("")
        self.label_2.setText(QCoreApplication.translate("StatsWindow", u"Statistics", None))
        self.label_3.setText(QCoreApplication.translate("StatsWindow", u"Scatterogram", None))
        self.label_4.setText(QCoreApplication.translate("StatsWindow", u"Histogram", None))
        self.label_5.setText(QCoreApplication.translate("StatsWindow", u"<html><head/><body><p>HR, <span style=\" font-size:11pt;\">bpm</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("StatsWindow", u"<html><head/><body><p>NN, <span style=\" font-size:14pt;\">ms</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("StatsWindow", u"<html><head/><body><p>SDNN, <span style=\" font-size:14pt;\">ms</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("StatsWindow", u"<html><head/><body><p>Mo, <span style=\" font-size:14pt;\">ms</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("StatsWindow", u"<html><head/><body><p>AMo, <span style=\" font-size:14pt;\">%</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("StatsWindow", u"<html><head/><body><p>MxDMn, <span style=\" font-size:14pt;\">ms</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("StatsWindow", u"PI", None))
    # retranslateUi

