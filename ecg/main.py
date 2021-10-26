import sys, time
import numpy as np

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

import matplotlib.pyplot as plt
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from main_window import *
from sub_window import *

random.seed(11)
plt.style.use('dark_background')
plt.rc('axes', axisbelow=True)


class Claw:
    def __init__(self, amp=0.0, mu=0.0, b1=0.0, b2=0.0):
        self.amp = amp
        self.mu = mu
        self.b1 = b1
        self.b2 = b2
        self.t1 = self.mu - 3 * self.b1
        self.t2 = self.mu + 3 * self.b2


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


class SubWindow(QMainWindow):
    def __init__(self, t, y, T):
        QMainWindow.__init__(self)
        self.ui = Ui_SubWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

        self.sub_canvas = Canvas(self.ui.EcgWideWidget)

        self.t, self.y, self.T = t, y, T

        self.rng = [random.randint(0, 1) for i in range(self.ui.spinBoxCount.value())]

        self.ui.AlternationHorisontalSlider.valueChanged.connect(self.draw_extend)
        self.ui.NoiseHorizontalSlider.valueChanged.connect(self.draw_extend)

        self.ui.pushButtonFilt.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButtonFilt_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.AlphaHorizontalSlider.valueChanged.connect(lambda: self.ui.label_alp.setText(f"{self.ui.AlphaHorizontalSlider.value()/100}"))
        self.ui.WidthHorizontalSlider.valueChanged.connect(lambda: self.ui.label_wdth.setText(f"{self.ui.WidthHorizontalSlider.value()}"))

        self.ui.radioButton.toggled.connect(self.exp_filter)
        self.ui.radioButton_2.toggled.connect(self.float_width)

        self.show()

    def draw_extend(self):
        y_alternate = np.copy(self.y)
        temp = self.t[int(self.T.t1 * 1000): int(self.T.t2 * 1000)]
        y_alternate[int(self.T.t1 * 1000): int(self.T.t2 * 1000)] = \
            self.T.amp * (1 + (self.ui.AlternationHorisontalSlider.value()/100)/self.T.amp) * \
            np.exp(-1 * (temp - self.T.mu) ** 2 / (2 * np.where(temp < self.T.mu, self.T.b1, self.T.b2) ** 2))

        x = np.arange(0.0, self.ui.spinBoxCount.value() * (len(self.t)/1000), 0.001)
        y = np.array([])

        for i in range(self.ui.spinBoxCount.value()):
            y = np.append(y, self.y if self.rng[i] else y_alternate)

        y = y + np.random.normal(0, self.ui.NoiseHorizontalSlider.value()/100, len(y))

        self.sub_canvas.ax.cla()
        self.sub_canvas.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")
        self.sub_canvas.ax.minorticks_on()
        self.sub_canvas.ax.set_ylim(min(self.y) - 0.1, max(self.y) + 0.1)
        self.sub_canvas.ax.plot(x, y, color="white", linewidth=1.5)
        self.sub_canvas.draw()

    def exp_filter(self):
        self.ui.AlphaHorizontalSlider.setEnabled(True)
        self.ui.WidthHorizontalSlider.setDisabled(True)

    def float_width(self):
        self.ui.AlphaHorizontalSlider.setDisabled(True)
        self.ui.WidthHorizontalSlider.setEnabled(True)

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
    hr = 0
    claws = {'P': Claw(), 'Q': Claw(), 'R': Claw(), 'S': Claw(), 'ST': Claw(), 'T': Claw()}

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

        self.ui.pushButtonGen.clicked.connect(self.generate)

        self.canvas = Canvas(self.ui.EcgWidget)

    # self.ui.AmplitudeHorizontalSlider.valueChanged.connect(lambda: print(self.ui.AmplitudeHorizontalSlider.value()))

        self.show()

    def claws_values(self, t):
        c = len(t)/1000
        mu = t[int(len(t)*0.4)]
        self.claws['P'] = Claw(0.1, mu, 0.02, 0.02)
        self.claws['Q'] = Claw(-0.1, self.claws['P'].t2 + 0.015 * c, 0.005 * c, 0.005 * c)
        self.claws['R'] = Claw(1.0, self.claws['Q'].t2 + 0.03 * c, 0.01 * c, 0.01 * c)
        self.claws['S'] = Claw(-0.17, self.claws['R'].t2 + 0.03 * c, 0.01 * c, 0.01 * c)
        self.claws['ST'] = Claw(0, self.claws['S'].t2 + 0.003 * c, 0.001 * c, 0.001 * c)
        self.claws['T'] = Claw(self.ui.AmplitudeHorizontalSlider.value()/10,
                               self.claws['ST'].t2 + (0.0425 + self.ui.TimeHorizontalSlider.value()/200) * c +
                               self.ui.B1HorizontalSlider.value()/100 * 3 * c,
                               self.ui.B1HorizontalSlider.value()/100 * c, self.ui.B2HorizontalSlider.value()/100 * c)

    def generate(self):

        self.canvas.ax.cla()

        self.hr = self.ui.spinBoxHr.value()
        t0 = 60/self.hr * 1000
        t = np.linspace(0, t0, int(t0))
        t /= 1000
        y = np.zeros(len(t))

        self.claws_values(t)

        for cr in self.claws.keys():
            clw = self.claws[cr]
            temp = t[int(clw.t1*1000): int(clw.t2*1000)]
            y[int(clw.t1*1000): int(clw.t2*1000)] = clw.amp * np.exp(-1 * (temp - clw.mu) ** 2 /
                                                                     (2 * np.where(temp < clw.mu, clw.b1, clw.b2) ** 2))
            if cr != "ST":
                self.canvas.ax.text(clw.mu, clw.amp + 0.07 if clw.amp > 0 else clw.amp - 0.01,
                                    cr, ha='center', va='top', c='white')

        self.canvas.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")

        plt.xticks(np.arange(0, t0/1000 + 0.1, 0.1))
        plt.yticks(np.arange(-1, 1.5, 0.1))

        self.canvas.ax.set_xlim(0, max(t))
        self.canvas.ax.set_ylim(min(y) - 0.1, max(y) + 0.1)

        self.canvas.ax.set_xlabel("Time, sec")
        self.canvas.ax.set_ylabel("Voltage, mV")

        self.canvas.ax.plot(t, y, color="white", linewidth=1.5)

        self.canvas.draw()

        self.sub_window = SubWindow(t=t, y=y, T=self.claws['T'])
        self.sub_window.draw_extend()

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
