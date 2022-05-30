import sys, os, time
import numpy as np

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

import matplotlib.pyplot as plt
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ui_ecg_graphs import *
from ui_ecg_portraits import *

plt.style.use('dark_background')
plt.rc('axes', axisbelow=True)
colors = ['white', 'yellow', 'red', 'blue']


def distance(x, y):
    return np.sqrt(np.sum((x - y)**2))


def hausdorff_distance(X, Y):
    return np.max([np.max([np.min([distance(x, y) for y in Y]) for x in X]),
                   np.max([np.min([distance(x, y) for x in X]) for y in Y])])


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
        # self.ax.set_ylim(min(y) - 0.1, max(y) + 0.1)
        if len(kwargs):
            self.ax.set_xlabel(kwargs['x_label'])
            self.ax.set_ylabel(kwargs['y_label'])
        self.ax.plot(x, y, color=color, linewidth=linewidth)

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


class PortraitMainWindow(QMainWindow):
    dz = []
    data = []

    def __init__(self, z):
        QMainWindow.__init__(self)
        self.ui = Ui_PortraitMainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)
        self.z = z

        self.differentiate()
        self.normalize()

        self.canvas = Canvas(self.ui.EcgWidget)

        self.draw_portraits()

        self.portraits = [np.array([self.dz[i], self.z[i]]).T for i in range(4)]

        self.ui.pushButtonCalc.clicked.connect(self.hausdorff_matrix)
        self.ui.pushButtonFind.clicked.connect(self.find_pivot)

    def draw_portraits(self):
        for i in range(4):
            self.canvas.draw_plot(self.dz[i], self.z[i], color=colors[i])

    def normalize(self):
        for i in range(4):
            self.z[i] = (self.z[i] - np.min(self.z[i]))/(np.max(self.z[i]) - np.min(self.z[i]))
            self.dz[i] = (self.dz[i] - np.min(self.dz[i]))/(np.max(self.dz[i]) - np.min(self.dz[i]))

    def differentiate(self):
        for z in self.z:
            dz = np.zeros(len(z))
            # dz = np.gradient(z, np.arange(0, len(z) / 500, 0.002))
            for i in range(3, len(z) - 3):
                dz[i] = (z[i + 3] - 9*z[i + 2] + 45*z[i + 1] - 45*z[i - 1] + 9*z[i - 2] - z[i - 3])/60

            self.dz.append(dz)

    def hausdorff_matrix(self):
        result = [[0]*4 for _ in range(4)]

        for i in range(4):
            for j in range(4):
                if i == j:
                    result[i][j] = 0
                    continue
                elif result[j][i] != 0:
                    result[i][j] = result[j][i]
                    continue
                else:
                    result[i][j] = hausdorff_distance(self.portraits[i], self.portraits[j])
        print(result)
        self.data = result
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)

    def find_pivot(self):
        idx = np.argmin([np.sum(x) for x in self.data])
        self.canvas.draw_plot(self.dz[idx], self.z[idx], color=colors[idx], linewidth=2.5)
        self.ui.tableView.selectRow(idx)

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
    ecgs = []

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
        self.ui.pushButtonNext.clicked.connect(self.next)

        self.ecg1 = Canvas(self.ui.EcgWidget_1)
        self.ecg2 = Canvas(self.ui.EcgWidget_2)
        self.ecg3 = Canvas(self.ui.EcgWidget_3)
        self.ecg4 = Canvas(self.ui.EcgWidget_4)

        ecgs = [self.ecg1, self.ecg2, self.ecg3, self.ecg4]

        self.read_data()

        for i in range(4):
            t = np.arange(0, len(self.ecgs[i]) / 500, 0.002)
            ecgs[i].draw_plot(t, self.ecgs[i], x_label="Time, sec", y_label="Voltage, mV", color=colors[i])

        self.show()

    def next(self):
        self.portrait_window = PortraitMainWindow(self.ecgs)
        self.close()
        time.sleep(0.5)
        self.portrait_window.show()

    def read_data(self):
        for i in range(4):
            with open(f"{i+1}.txt", 'r') as f:
                z = []
                for line in f:
                    line = line.strip()
                    z += line.split(" ")

                z = list(filter(None, z))
                z = list(map(float, z))
                self.ecgs.append(np.array(z))

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
