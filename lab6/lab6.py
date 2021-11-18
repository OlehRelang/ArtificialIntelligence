import sys, os, time
import numpy as np

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

import matplotlib.pyplot as plt
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ui_lab6_mw import *
from ui_lab6_ww import *

plt.style.use('dark_background')
plt.rc('axes', axisbelow=True)


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(parent.width()/100, parent.height()/100),
                                         facecolor='#1c1f23', edgecolor="#1c1f23")
        # self.fig.tight_layout()
        self.ax.set_facecolor('#1c1f23')
        self.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")
        # self.ax.grid(True, which="minor", color="#c2c2c2", linestyle="--")
        self.ax.minorticks_on()
        super().__init__(self.fig)
        self.setParent(parent)

    def draw_plot(self, x, y, **kwargs):
        self.ax.cla()
        self.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")
        self.ax.minorticks_on()
        # self.ax.set_xlim(0, max(x))
        # self.ax.set_ylim(min(y) - 0.1, max(y) + 0.1)
        self.ax.set_xlabel(kwargs['x_label'])
        self.ax.set_ylabel(kwargs['y_label'])
        self.ax.plot(x, y, color="white", linewidth=1.5)

        self.draw()


class MainWorkWindow(QMainWindow):
    def __init__(self, z):
        self.z = z
        QMainWindow.__init__(self)
        self.ui = Ui_MainWorkWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

        self.ui.TauHorizontalSlider.valueChanged.connect(self.plt2)

        self.ecg_canvas = Canvas(self.ui.EcgWidget)
        self.phase_portrait1 = Canvas(self.ui.PP1Widget)
        self.phase_portrait2 = Canvas(self.ui.PP2Widget)

        t = np.arange(0, len(self.z) / 500, 0.002)
        self.ecg_canvas.draw_plot(t, self.z, x_label="Time", y_label="Voltage, mV")
        self.phase_portrait1.draw_plot(np.gradient(np.array(self.z), t), self.z, x_label="dz/dt", y_label="z")
        self.phase_portrait2.draw_plot(self.z, self.z, x_label="z(t)", y_label="z(t-τ)")

        self.ui.pushButtonBack.clicked.connect(self.back)
        # self.show()

    def back(self):
        self.close()
        time.sleep(0.5)
        self.wind = MainWindow()

    def plt2(self):
        self.ui.label_tau.setText(str(self.ui.TauHorizontalSlider.value()))
        self.phase_portrait2.draw_plot(self.z, self.z[-self.ui.TauHorizontalSlider.value():] +
                                       self.z[:-self.ui.TauHorizontalSlider.value()], x_label="z(t)", y_label="z(t-τ)")

    def mousePressEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


class MainWindow(QMainWindow):
    z = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

        self.ui.pushButtonNext.setVisible(False)
        self.ui.pushButtonNext.clicked.connect(self.next)

        self.setAcceptDrops(True)

        self.show()

    def next(self):
        self.workWindow = MainWorkWindow(z=self.z)
        self.workWindow.show()
        self.close()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        self.ui.label_drop.setText(f"Table uploaded\n {os.path.split(files[0])[1]}")
        self.ui.pushButtonNext.setVisible(True)
        with open(files[0], 'r') as f:
            z = []
            for line in f:
                line = line.strip()
                z += line.split(" ")

            z = list(filter(None, z))
            z = list(map(float, z))
            self.z = z

    def mousePressEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    app = QApplication.instance()
    if app == None:
        app = QApplication()
    window = MainWindow()
    sys.exit(app.exec_())
