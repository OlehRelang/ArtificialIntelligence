# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab3EBYCnQ.ui'
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
        MainWindow.resize(1119, 704)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(MainWindow)
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
        self.EcgWidget = QWidget(self.centralwidget)
        self.EcgWidget.setObjectName(u"EcgWidget")
        self.EcgWidget.setGeometry(QRect(30, 80, 1060, 391))
        self.EcgWidget.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 15px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 35, 350, 41))
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
        self.frame_teeth = QFrame(self.centralwidget)
        self.frame_teeth.setObjectName(u"frame_teeth")
        self.frame_teeth.setGeometry(QRect(740, 520, 351, 161))
        self.frame_teeth.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.frame_teeth.setFrameShape(QFrame.StyledPanel)
        self.frame_teeth.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_teeth)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(18, 20, 321, 121))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(100)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(82, 0, 7, 0)
        self.radioButton_P = QRadioButton(self.widget)
        self.radioButton_P.setObjectName(u"radioButton_P")
        self.radioButton_P.setMaximumSize(QSize(41, 17))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.radioButton_P.setFont(font2)
        self.radioButton_P.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioButton_P)

        self.radioButton_S = QRadioButton(self.widget)
        self.radioButton_S.setObjectName(u"radioButton_S")
        self.radioButton_S.setMaximumSize(QSize(41, 17))
        self.radioButton_S.setFont(font2)
        self.radioButton_S.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.radioButton_S)

        self.radioButton_Q = QRadioButton(self.widget)
        self.radioButton_Q.setObjectName(u"radioButton_Q")
        self.radioButton_Q.setMaximumSize(QSize(41, 17))
        self.radioButton_Q.setFont(font2)
        self.radioButton_Q.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.radioButton_Q)

        self.radioButton_ST = QRadioButton(self.widget)
        self.radioButton_ST.setObjectName(u"radioButton_ST")
        self.radioButton_ST.setMaximumSize(QSize(41, 17))
        self.radioButton_ST.setFont(font2)
        self.radioButton_ST.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.radioButton_ST)

        self.radioButton_R = QRadioButton(self.widget)
        self.radioButton_R.setObjectName(u"radioButton_R")
        self.radioButton_R.setMaximumSize(QSize(41, 17))
        self.radioButton_R.setFont(font2)
        self.radioButton_R.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.radioButton_R)

        self.radioButton_T = QRadioButton(self.widget)
        self.radioButton_T.setObjectName(u"radioButton_T")
        self.radioButton_T.setMaximumSize(QSize(41, 17))
        self.radioButton_T.setFont(font2)
        self.radioButton_T.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.radioButton_T)

        self.frame_params = QFrame(self.centralwidget)
        self.frame_params.setObjectName(u"frame_params")
        self.frame_params.setGeometry(QRect(140, 500, 581, 181))
        self.frame_params.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.frame_params.setFrameShape(QFrame.StyledPanel)
        self.frame_params.setFrameShadow(QFrame.Raised)
        self.AmplitudeHorizontalSlider = QSlider(self.frame_params)
        self.AmplitudeHorizontalSlider.setObjectName(u"AmplitudeHorizontalSlider")
        self.AmplitudeHorizontalSlider.setGeometry(QRect(250, 20, 301, 22))
        self.AmplitudeHorizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.AmplitudeHorizontalSlider.setMinimum(-10)
        self.AmplitudeHorizontalSlider.setMaximum(10)
        self.AmplitudeHorizontalSlider.setOrientation(Qt.Horizontal)
        self.label_5 = QLabel(self.frame_params)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 15, 241, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.TimeHorizontalSlider = QSlider(self.frame_params)
        self.TimeHorizontalSlider.setObjectName(u"TimeHorizontalSlider")
        self.TimeHorizontalSlider.setGeometry(QRect(250, 50, 301, 22))
        self.TimeHorizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.TimeHorizontalSlider.setMinimum(-10)
        self.TimeHorizontalSlider.setMaximum(10)
        self.TimeHorizontalSlider.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.frame_params)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 45, 241, 31))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.B1HorizontalSlider = QSlider(self.frame_params)
        self.B1HorizontalSlider.setObjectName(u"B1HorizontalSlider")
        self.B1HorizontalSlider.setGeometry(QRect(150, 120, 301, 22))
        self.B1HorizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.B1HorizontalSlider.setMinimum(0)
        self.B1HorizontalSlider.setMaximum(10)
        self.B1HorizontalSlider.setOrientation(Qt.Horizontal)
        self.B2HorizontalSlider = QSlider(self.frame_params)
        self.B2HorizontalSlider.setObjectName(u"B2HorizontalSlider")
        self.B2HorizontalSlider.setGeometry(QRect(150, 150, 301, 22))
        self.B2HorizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.B2HorizontalSlider.setMinimum(0)
        self.B2HorizontalSlider.setMaximum(10)
        self.B2HorizontalSlider.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.frame_params)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 80, 301, 31))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.frame_hr = QFrame(self.centralwidget)
        self.frame_hr.setObjectName(u"frame_hr")
        self.frame_hr.setGeometry(QRect(20, 520, 101, 61))
        self.frame_hr.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.frame_hr.setFrameShape(QFrame.StyledPanel)
        self.frame_hr.setFrameShadow(QFrame.Raised)
        self.spinBoxHr = QSpinBox(self.frame_hr)
        self.spinBoxHr.setObjectName(u"spinBoxHr")
        self.spinBoxHr.setGeometry(QRect(11, 11, 81, 41))
        self.spinBoxHr.setFont(font2)
        self.spinBoxHr.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
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
        self.spinBoxHr.setFrame(True)
        self.spinBoxHr.setAlignment(Qt.AlignCenter)
        self.spinBoxHr.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxHr.setAccelerated(False)
        self.spinBoxHr.setProperty("showGroupSeparator", False)
        self.spinBoxHr.setMaximum(200)
        self.spinBoxHr.setValue(60)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 500, 101, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(740, 500, 351, 31))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pushButtonGen = QPushButton(self.centralwidget)
        self.pushButtonGen.setObjectName(u"pushButtonGen")
        self.pushButtonGen.setGeometry(QRect(20, 600, 101, 81))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButtonGen.setFont(font3)
        self.pushButtonGen.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonGen.setStyleSheet(u"QPushButton {\n"
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ECG Generator", None))
        self.radioButton_P.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.radioButton_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.radioButton_Q.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.radioButton_ST.setText(QCoreApplication.translate("MainWindow", u"ST", None))
        self.radioButton_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.radioButton_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043c\u043f\u043b\u0456\u0442\u0443\u0434\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.spinBoxHr.setSuffix("")
        self.spinBoxHr.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0421\u0421", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0443\u0431\u0446\u0456", None))
        self.pushButtonGen.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

