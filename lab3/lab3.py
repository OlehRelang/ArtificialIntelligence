import sys, time
import numpy as np

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ui_lab3 import *

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

    def calc_time(self):
        self.t1 = self.mu - 3 * self.b1
        self.t2 = self.mu + 3 * self.b2


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(10.6, 3.91), facecolor='#1c1f23', edgecolor="#1c1f23")
        # self.fig.tight_layout()
        self.ax.set_facecolor('#1c1f23')
        self.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")
        # self.ax.grid(True, which="minor", color="#c2c2c2", linestyle="--")
        self.ax.minorticks_on()
        super().__init__(self.fig)
        self.setParent(parent)


class MainWindow(QMainWindow):
    hr = 0
    claws = {'P': Claw(), 'Q': Claw(), 'R': Claw(), 'S': Claw(), 'T': Claw()}
    # claws = {'P': Claw(0.1, 0.4, 0.02, 0.02),
    #          'Q': Claw(-0.1, 0.475, 0.005, 0.005),
    #          'R': Claw(1.0, 0.52, 0.01, 0.01),
    #          'S': Claw(-0.17, 0.58, 0.01, 0.01),
    #          'T': Claw(0.2, 0.78, 0.02, 0.02)}

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
        self.claws['T'] = Claw(self.ui.AmplitudeHorizontalSlider.value()/10,
                               self.claws['S'].t2 + (0.06 + self.ui.TimeHorizontalSlider.value()/200) * c +
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
            plt.text(clw.mu, clw.amp + 0.07 if clw.amp > 0 else clw.amp - 0.01, cr, ha='center', va='top', c='white')

        self.canvas.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")

        plt.xticks(np.arange(0, t0/1000 + 0.1, 0.1))
        plt.yticks(np.arange(-1, 1.5, 0.1))

        self.canvas.ax.set_xlim(0, max(t))
        self.canvas.ax.set_ylim(min(y) - 0.1, max(y) + 0.1)

        self.canvas.ax.set_xlabel("Time, sec")
        self.canvas.ax.set_ylabel("Voltage, mV")

        self.canvas.ax.plot(t, y, color="white", linewidth=1.5)

        self.canvas.draw()

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
