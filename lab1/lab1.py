import sys, time

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

import random

from threading import Thread

from ui_lab1 import *


class MainWindow(QMainWindow):
    user_text = ''
    btn = False

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

        self.ui.pushButtonSemd.clicked.connect(self.send_message)
        self.ui.pushButton.clicked.connect(self.stop)

        self.t = Thread(target=self.dialog, daemon=True)

        self.t.start()

        self.show()

    def stop(self):
        self.ui.label_5.setText("Вы меня раскусили!")
        self.ui.pushButtonSemd.setEnabled(False)
        self.ui.pushButton.setEnabled(False)

    def wait(self):
        self.btn = False
        while not self.btn:
            time.sleep(1)

    def dialog(self):
        time.sleep(2)

        self.ui.label_5.setText("Привет, как вас зовут?")
        self.wait()
        self.ui.label_5.setText(f"Привет, {self.user_text}")

        time.sleep(2)

        self.ui.label_5.setText("Вы бинарного гендера?")
        self.wait()
        if self.user_text in ["Да", "Конечно"]:
            self.ui.label_5.setText("Здорово")
            time.sleep(2)

            while True:
                self.ui.label_5.setText("Вы М или Ж?")
                self.wait()
                if self.user_text in ["М", "Мужской"]:
                    self.ui.label_5.setText("Ммммм... Сильный пол,\nпрекрасно")
                    break
                elif self.user_text in ["Ж", "Женский"]:
                    self.ui.label_5.setText("Прекрасный пол, чудесно")
                    break
                else:
                    self.ui.label_5.setText(random.choice(["Вы же говорили что бинарный.\nНаверно где-то ошибка?",
                                                           "Не понял.\nНаверно где-то ошибка?",
                                                           "Вы уверены?"]))
                    time.sleep(2)
        else:
            self.ui.label_5.setText("Кхм... Ладно, проехали.")

        time.sleep(2)

        self.ui.label_5.setText("Сколько Вам лет?")
        self.wait()
        if int(self.user_text) > 30:
            self.ui.label_5.setText("Ого, вы намного старше меня")
        else:
            self.ui.label_5.setText("Круто, между нами не такая уж\nи большая разница в возрасте")

        time.sleep(2)

        self.ui.label_5.setText("У вас есть домашнее животное?")
        self.wait()
        if self.user_text in ["Да", "Есть"]:
            self.ui.label_5.setText("А какое?")
            self.wait()
            self.ui.label_5.setText(random.choice(["Как мило.", "Прикольно)"]))
        else:
            self.ui.label_5.setText("Эх... А вот мне нравятся\n " + random.choice(["кошки", "собаки",
                                                                                   "попугаи", "выдры"]))

        time.sleep(2)

        self.ui.label_5.setText('Вы смотрели "Игру Престолов"?')
        self.wait()
        if self.user_text in ["Да", "Конечно", "Ещё бы"]:
            self.ui.label_5.setText("И как, вам понравилось?")
            self.wait()
            if self.user_text in ["Да", "Конечно", "Ещё бы"]:
                self.ui.label_5.setText("Мне тоже, правда 7 и 8\nсезоны были так себе.")
            else:
                self.ui.label_5.setText("Ну, у всех свои вкусы")
        elif self.user_text == "Нет":
            self.ui.label_5.setText("Зря, советую посмотреть\nМне лично очень понравилось")

        time.sleep(2)

        self.ui.label_5.setText("Вам нравится рок музыка?")
        self.wait()
        if self.user_text in ["Да", "Конечно", "Ещё бы"]:
            self.ui.label_5.setText("Мне тоже")
            time.sleep(2)
            self.ui.label_5.setText("Какой ваш самый любимый\nисполнитель?")
            self.wait()
            singers = ["The Beatles", "Queen", "Led Zeppelin", "Deep Purple", "The Animals"]
            rsinger = random.choice(singers)
            if self.user_text == rsinger:
                self.ui.label_5.setText("О, и мой тоже)")
            else:
                self.ui.label_5.setText(f"Круто, а мне вот нравятся\n{rsinger}")
        else:
            self.ui.label_5.setText("Ну и ладно")

        time.sleep(2)

        self.ui.label_5.setText("И напоследок...")
        time.sleep(2)
        self.ui.label_5.setText("В чём сила?")
        self.wait()
        if self.user_text == "В правде":
            self.ui.label_5.setText("Неплохо)")
        else:
            self.ui.label_5.setText(")))")

        time.sleep(2)

        self.ui.label_5.setText("Что ж, мне пора закруглятся.")
        time.sleep(2)
        self.ui.label_5.setText("Было приятно пообщатся.\nНадеюсь ещё спишемся)")
        time.sleep(2)
        self.ui.label_5.setText("...")
        self.ui.pushButtonSemd.setEnabled(False)

    def send_message(self):
        self.ui.labelPoints.setText(str(int(self.ui.labelPoints.text()) + 1))
        self.user_text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText("")
        self.btn = True

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
