import sys, os, time
import numpy as np

from statistics import mode

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

import matplotlib.pyplot as plt
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ui_main_window import *
from ui_stats_window import *

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

    def draw_plot(self, x, y, color="white", linewidth=1.5, **kwargs):
        # self.ax.cla()
        self.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")
        self.ax.minorticks_on()
        # self.ax.set_xlim(0, max(x))
        self.ax.set_ylim([600, 1400])
        if len(kwargs):
            self.ax.set_xlabel(kwargs['x_label'])
            self.ax.set_ylabel(kwargs['y_label'])
        self.ax.plot(x, y, color=color, linewidth=linewidth)

    def draw_scatter(self, x, y, color="white", **kwargs):
        self.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")
        self.ax.minorticks_on()
        self.ax.set_xlim([600, 1400])
        self.ax.set_ylim([600, 1400])
        if len(kwargs):
            self.ax.set_xlabel(kwargs['x_label'])
            self.ax.set_ylabel(kwargs['y_label'])
        self.ax.scatter(x, y, color=color)

    def draw_hist(self, x, color="white", width=1.0, **kwargs):
        # self.ax.cla()
        self.ax.grid(True, which='major', color='#c2c2c2', linestyle="-")
        self.ax.minorticks_on()
        # self.ax.set_xlim(0, max(x))
        # self.ax.set_ylim([600, 1400])
        if len(kwargs):
            self.ax.set_xlabel(kwargs['x_label'])
            self.ax.set_ylabel(kwargs['y_label'])
        self.ax.hist(x, bins=np.arange(600, 1420, 20), color=color, rwidth=width, range=(600, 1400))

        self.draw()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        # self.setParent(parent)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, float):
                return "%.3f" % value

            return value

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class StatsWindow(QMainWindow):
    data = [[60.151, 900.512, 500.214, 900.148, 65.74, 400.542, 400]]

    def __init__(self, rhythm):
        QMainWindow.__init__(self)
        self.ui = Ui_StatsWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButtonClose.clicked.connect(self.close)
        self.ui.pushButtonExp.clicked.connect(self.showMinimized)

        self.rhythm = rhythm

        self.scatter = Canvas(self.ui.ScatterWidget)
        self.hist = Canvas(self.ui.HistWidget)

        self.process_signal()

        self.show()

    def process_signal(self):
        rhythm1 = np.concatenate([np.array([self.rhythm[-1]]), self.rhythm[:-1]])
        self.scatter.draw_scatter(rhythm1, self.rhythm)
        self.scatter.draw_plot([0, 1400], [0, 1400], x_label="R-R[i+1], ms", y_label="R-R, ms")

        self.hist.draw_hist(self.rhythm, width=0.8, x_label="R-R, ms", y_label="Count")

        hr = (len(self.rhythm)*60)/(np.sum(self.rhythm)*0.001)
        nn = np.mean(self.rhythm)
        sdnn = np.sqrt(np.sum((self.rhythm - nn)**2)/len(self.rhythm))
        mo = mode(self.rhythm)
        amo = np.sum(np.where(self.rhythm == mo, 1, 0))/len(self.rhythm) * 100
        h = np.max(self.rhythm) - np.min(self.rhythm)
        pi = amo/(2*mo*h*10**(-6))
        print(pi)

        data = [[hr, nn, sdnn, mo, amo, h, pi]]

        self.model = TableModel(data)
        self.ui.tableView.setModel(self.model)

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
    rhythms = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButtonClose.clicked.connect(self.close)
        self.ui.pushButtonExp.clicked.connect(self.showMinimized)

        self.ui.pushButtonTo2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButtonTo1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.rhg1 = Canvas(self.ui.RhythmoWidget_1)
        self.rhg2 = Canvas(self.ui.RhythmoWidget_2)

        self.ui.pushButtonStat.clicked.connect(self.stats)

        self.read_data()
        self.draw_rhythmos()

        self.show()

    def draw_rhythmos(self):
        self.rhg1.draw_plot(np.arange(0, len(self.rhythms[0])), self.rhythms[0], x_label="Count", y_label="Duration, ms")
        self.rhg2.draw_plot(np.arange(0, len(self.rhythms[1])), self.rhythms[1], x_label="Count", y_label="Duration, ms")

    def stats(self):
        self.stats_view = StatsWindow(self.rhythms[self.ui.stackedWidget.currentIndex()])

    def read_data(self):
        for i in range(2):
            with open(f"Ритм {i+1}.txt", 'r') as f:
                z = []
                for line in f:
                    line = line.strip()
                    z += line.split(" ")

                z = list(filter(None, z))
                z = list(map(float, z))
                self.rhythms.append(np.array(z))

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
