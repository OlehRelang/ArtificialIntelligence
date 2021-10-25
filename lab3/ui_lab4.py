# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab4rLIWcw.ui'
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


class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        if SubWindow.objectName():
            SubWindow.setObjectName(u"SubWindow")
        SubWindow.resize(1120, 580)
        SubWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(SubWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 1119, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(1080, 8, 15, 15))
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
        self.pushButton_close.setGeometry(QRect(1100, 8, 16, 16))
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
        self.EcgWideWidget = QWidget(self.centralwidget)
        self.EcgWideWidget.setObjectName(u"EcgWideWidget")
        self.EcgWideWidget.setGeometry(QRect(30, 60, 1061, 391))
        self.EcgWideWidget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.frame_params = QFrame(self.centralwidget)
        self.frame_params.setObjectName(u"frame_params")
        self.frame_params.setGeometry(QRect(30, 470, 1061, 91))
        self.frame_params.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.frame_params.setFrameShape(QFrame.StyledPanel)
        self.frame_params.setFrameShadow(QFrame.Raised)
        self.AlternationHorisontalSlider = QSlider(self.frame_params)
        self.AlternationHorisontalSlider.setObjectName(u"AlternationHorisontalSlider")
        self.AlternationHorisontalSlider.setGeometry(QRect(280, 50, 301, 22))
        self.AlternationHorisontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.AlternationHorisontalSlider.setMinimum(-10)
        self.AlternationHorisontalSlider.setMaximum(10)
        self.AlternationHorisontalSlider.setOrientation(Qt.Horizontal)
        self.label_5 = QLabel(self.frame_params)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(313, 12, 241, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_params)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(727, 12, 241, 31))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.NoiseHorizontalSlider = QSlider(self.frame_params)
        self.NoiseHorizontalSlider.setObjectName(u"NoiseHorizontalSlider")
        self.NoiseHorizontalSlider.setGeometry(QRect(690, 50, 301, 22))
        self.NoiseHorizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.NoiseHorizontalSlider.setMinimum(0)
        self.NoiseHorizontalSlider.setMaximum(10)
        self.NoiseHorizontalSlider.setOrientation(Qt.Horizontal)
        self.spinBoxCount = QSpinBox(self.frame_params)
        self.spinBoxCount.setObjectName(u"spinBoxCount")
        self.spinBoxCount.setGeometry(QRect(90, 40, 81, 41))
        self.spinBoxCount.setFont(font1)
        self.spinBoxCount.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(28, 31, 35);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"	\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
";\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off { /* off state when value in min */\n"
"\n"
"}")
        self.spinBoxCount.setFrame(True)
        self.spinBoxCount.setAlignment(Qt.AlignCenter)
        self.spinBoxCount.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxCount.setAccelerated(False)
        self.spinBoxCount.setProperty("showGroupSeparator", False)
        self.spinBoxCount.setMaximum(120)
        self.spinBoxCount.setValue(30)
        self.label_3 = QLabel(self.frame_params)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 12, 141, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        SubWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SubWindow)

        QMetaObject.connectSlotsByName(SubWindow)
    # setupUi

    def retranslateUi(self, SubWindow):
        SubWindow.setWindowTitle(QCoreApplication.translate("SubWindow", u"MainWindow", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_5.setText(QCoreApplication.translate("SubWindow", u"\u0420\u0456\u0432\u0435\u043d\u044c \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0446\u0456\u0457", None))
        self.label_6.setText(QCoreApplication.translate("SubWindow", u"\u0420\u0456\u0432\u0435\u043d\u044c \u0448\u0443\u043c\u0443", None))
        self.spinBoxCount.setSuffix("")
        self.spinBoxCount.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("SubWindow", u"\u041a-\u0442\u044c \u0446\u0438\u043a\u043b\u0456\u0432", None))
    # retranslateUi

