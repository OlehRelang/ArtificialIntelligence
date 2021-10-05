import sys, time, datetime
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from functools import partial
import random

from ui_lab2 import *


class MainWindow(QMainWindow):

    signs = {1: "Водолій", 2: "Риби", 3: "Овен", 4: "Телець", 5: "Близнюки", 6: "Рак", 7: "Лев", 8: "Діва", 9: "Ваги",
             10: "Скорпіон", 11: "Стрілець", 12: "Козеріг"}
    sign_id = 0

    day_p = {}
    week_p = {}
    month_p = {}

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

        self.sign_buttons = {1: self.ui.pushButton1, 2: self.ui.pushButton2, 3: self.ui.pushButton3,
                             4: self.ui.pushButton4, 5: self.ui.pushButton5, 6: self.ui.pushButton6,
                             7: self.ui.pushButton7, 8: self.ui.pushButton8, 9: self.ui.pushButton9,
                             10: self.ui.pushButton10, 11: self.ui.pushButton11, 12: self.ui.pushButton12}

        for key, value in self.sign_buttons.items():
            value.clicked.connect(partial(self.click, num=key, sign=value.text()))

        self.ui.pushButton2_2.clicked.connect(partial(self.prediction, t=1))
        self.ui.pushButton2_3.clicked.connect(partial(self.prediction, t=2))
        self.ui.pushButton2_4.clicked.connect(partial(self.prediction, t=0))

        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(
            (self.ui.stackedWidget.currentIndex() + 1) % 2))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(
            (self.ui.stackedWidget.currentIndex() + 1) % 2))

        self.ui.pushButtonSend.clicked.connect(self.sign_by_date)

        self.show()

    def sign_by_date(self):
        day, month, _ = self.ui.lineEdit.text().split(".")

        if int(day) < 21:
            if int(month) - 1 == 0:
                self.ui.pushButton12.click()
            else:
                self.sign_buttons[(int(month) - 1)].click()
        else:
            self.sign_buttons[int(month)].click()

    def prediction(self, t):

        if not self.sign_id:
            return

        good = ['Життєві негаразди і труднощі, перед\nякими багатохто здає свої позиції,\nне зіб\'ють вас зі '
                'шляху.\nНе сподівайтеся на випадок,\nрозраховувати потрібно лише на себе,\nа астрологічні умови '
                'нинішньої доби\nдопоможуть вам вдало завершити\nрозпочате.',
                'Тільки ви здатні самостійно\nзорієнтуватися в тому, що\nвідбувається, '
                'але обов\'язково\nподолаєте в собі бажання бути\nцентром загальної уваги,'
                '\nсьогодні це зовсім не потрібно.',
                'Ви наполегливі і готові\nвідстоювати свою точку зору.\n'
                'У цей період важливо планувати\nкожен свій крок. Знайдіть мотиви,\n'
                'які змусять вас перейти від\nтеорії до практики.',
                'Сформована астрологічна ситуація\nобіцяє гармонійний розвиток подій\nі матеріальне благополуччя.\n'
                'Обставини надають вам\nможливість досягти успіху\nбуквально у будь-якомій справі.',
                f'Сприятливий час для представників\nзнака Зодіаку {self.signs[self.sign_id]}.\n'
                f'Удача сама йде в руки, і головне\nне відмахуватися від неї, та й не\nпройти самому повз.']

        bad = ["Незважаючи на сприятливу для\nвашого знаку фазу місяця, вам\nпотрібно бути дуже обачливим з\n"
               "вашими бажаннями. Необдуманно\nвикинуте слово може мати\nнегативні та далеко йдущі\n"
               "наслідки для вас.",
               "Життя складається з чорних та\nбілих полос, нажаль для вас\nнастала чорна. Щоб мінімізувати\n"
               "можливі наслідки варто\nприслуховуватись до старших, бути\nдуже обачливим та не робити того,\n"
               "у чому не впевнені на сто відсотків.",
               "Найближчим часом на вас чекають\nнові випробування. Запасіться\nтерпінням та силами для їх\n"
               "подолання, адже незважаючи на те\nщо нагорода буде незначною, у\nразі невдачі наслідки можуть бути"
               "\nсерйозними."]

        filler = ["Не слід активно\nвідстоювати свої інтереси, якщо\nбажаєте зберегти позиції.\n"
                  "Вам зараз необхідно сильне плече,\nна яке можна не тільки спертися,\nа й перекласти "
                  "тягар своїх турбот.\tПідшукайте в оточенні гідного\nкандидата на цю роль, він\nобов'язково "
                  "знайдеться, можливо,\nсеред представників протилежної\nстаті. "
                  "Однак не слід надавати\nподібним діям романтичного сенсу,\nінакше можна все зіпсувати.",
                  "Ймовірно поява нової людини в\nвашому оточенні, і інтерес до\nнеї буде настільки сильний,\n"
                  "що неодмінно захочеться\tпознайомитися ближче. Але не слід\nдіяти дуже відкрито, "
                  "подібна\nтактика в поточний момент матиме\nвельми сумнівний успіх, "
                  "більш\nефективним буде делікатний шлях.",
                  "В даний момент в усьому, що\nстосується побуту, не слід\nприймати рішення самому,\nкраще "
                  "присвятити в свої плани\nтих, хто живе поруч з вами\tі отримати їх підтримку в певних\n"
                  "ваших діях. Підшукайте час\nзаглянути до сусідів, ймовірно,\nви дізнаєтеся щось нове, якусь\n"
                  "таємницю або секрет,\nщодовашої персони."]

        ending = [f"У другій половині напружена\nробота напевно послабить ваші\nсили, проте грошові "
                  "перспективи\nстануть яснішими.",
                  f"У другій половині чекайте\nцікавих зустрічей, також\nнамагайтеся "
                  "бути обережними,\nв іншому випадку неприємностей\nне уникнути."]

        if t == 1:

            if self.sign_id in self.day_p.keys():
                self.ui.label_text.setText(self.day_p[self.sign_id][0])
                self.ui.label_text_2.setText(self.day_p[self.sign_id][1])
                return

            self.ui.label_date.setText(str(datetime.datetime.now().strftime("%d.%m.%Y")))
            choice1 = random.choice(['хороший', 'поганий'])
            self.ui.label_text.setText(f"Сьогодні на вас чекає {choice1} день.")

            if choice1 == 'хороший':
                self.ui.label_text.setText(self.ui.label_text.text() + f'\n{random.choice(good)}')
            else:
                self.ui.label_text.setText(self.ui.label_text.text() + f'\n{random.choice(bad)}')

            f_choice = random.choice(filler).split("\t")

            self.ui.label_text.setText(self.ui.label_text.text() + f'\n{f_choice[0]}')
            self.ui.label_text_2.setText(f'{f_choice[1]}' + f'\n{random.choice(ending)}')

            self.day_p[self.sign_id] = [self.ui.label_text.text(), self.ui.label_text_2.text()]

        elif t == 2:

            if self.sign_id in self.week_p.keys():
                self.ui.label_text.setText(self.week_p[self.sign_id][0])
                self.ui.label_text_2.setText(self.week_p[self.sign_id][1])
                return

            self.ui.label_date.setText(datetime.datetime.now().strftime("%d.%m.%Y") + "-" +
                                       (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%d.%m.%Y")
                                       )
            choice2 = random.choice(["хороший", "важкий"])
            self.ui.label_text.setText(f"На вас чекає {choice2} тиждень.")

            if choice2 == 'хороший':
                self.ui.label_text.setText(self.ui.label_text.text() + f'\n{random.choice(good)}')
            else:
                self.ui.label_text.setText(self.ui.label_text.text() + f'\n{random.choice(bad)}')

            f_choice = random.choice(filler).split("\t")

            self.ui.label_text.setText(self.ui.label_text.text() + f'\n{f_choice[0]}')
            self.ui.label_text_2.setText(f'{f_choice[1]}' + f'\n{random.choice(ending)}')

            self.week_p[self.sign_id] = [self.ui.label_text.text(), self.ui.label_text_2.text()]

        else:

            if self.sign_id in self.month_p.keys():
                self.ui.label_text.setText(self.month_p[self.sign_id][0])
                self.ui.label_text_2.setText(self.month_p[self.sign_id][1])
                return

            self.ui.label_date.setText(datetime.datetime.now().strftime("%B %Y"))
            choice3 = random.choice(["сприятливий", "важкий"])
            self.ui.label_text.setText(f"На вас чекає {choice3} місяць.")

            if choice3 == 'сприятливий':
                self.ui.label_text.setText(self.ui.label_text.text() + f'\n{random.choice(good)}')
            else:
                self.ui.label_text.setText(self.ui.label_text.text() + f'\n{random.choice(bad)}')

            f_choice = random.choice(filler).split("\t")

            self.ui.label_text.setText(self.ui.label_text.text() + f'\n{f_choice[0]}')
            self.ui.label_text_2.setText(f'{f_choice[1]}' + f'\n{random.choice(ending)}')

            self.month_p[self.sign_id] = [self.ui.label_text.text(), self.ui.label_text_2.text()]

        self.ui.label_sign_name.setText(self.signs[self.sign_id])

    def click(self, num, sign):
        self.sign_id = num
        self.ui.label_sign.setText(sign)

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

