import sys
import sqlite3
import re
import string
import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QApplication
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pyqtgraph


# Main class
class BioStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWin = MainMenu()
        self.startWin = StartWindow()
        self.statisticWin = StatisticWindow()
        self.progInfo = ProgramInformation()
        self.dialogWin = DialogCount()
        self.resultWin = Result()


# Main menu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()
        self.show()

    def init_UI(self):
        # Установка фона
        set_background(self)

        # Загрузка GUI
        uic.loadUi('main.ui', self)

        # Подкличение функционала к кнопкам
        self.pushStart.clicked.connect(self.starting)
        self.pushStatistic.clicked.connect(self.show_statistic)
        self.pushAbout.clicked.connect(self.show_program_info)
        self.pushClean.clicked.connect(self.clean_progress)

    def starting(self):
        global prog

        prog.startWin.show()  # Запуск окна старта
        self.hide()

    def show_statistic(self):
        global prog

        prog.statisticWin.show()  # Запуск окна статистики
        self.hide()

    def show_program_info(self):
        global prog

        prog.progInfo.show()
        self.hide()

    def clean_progress(self):
        HISTORY.clear()
        with open('DATABASE.txt', 'w') as db:
            db.write('')


# Window start
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        # Установка фона
        set_background(self)

        # Загрузка GUI
        uic.loadUi('start.ui', self)

        self.productSlider.setMinimum(0)
        self.productSlider.setMaximum(30)
        self.productSlider.setValue(30)
        self.productSlider.valueChanged.connect(self.move_slider)
        self.productSlider.hide()

        self.hide_products()

        self.pushBackFromStart.clicked.connect(lambda: back_to_main(self))
        self.pushOkSearch.clicked.connect(self.searching)
        self.buttonGroup.buttonClicked.connect(self.add_count)

    def move_slider(self):
        size = len(self.needs) - self.productSlider.value()
        self.hide_products()
        for i in range(1, min(8, len(self.needs) + 1 - size)):
            eval('self.pushProduct_' + str(i) + '.setText(self.needs[i - 1 + ' + str(size) + '])')
            eval('self.pushProduct_' + str(i) + '.show()')

    def searching(self):  # Search button
        text = self.textSearch.toPlainText()
        self.needs = []
        for item in PRODUCTS_DICT:
            if clearWord(text.lower()) in item:
                self.needs.append(item)
        print(self.needs)

        self.productSlider.setMaximum(len(self.needs))
        self.productSlider.setValue(len(self.needs))

        self.hide_products()
        self.productSlider.show()
        for i in range(1, min(8, len(self.needs) + 1)):
            eval('self.pushProduct_' + str(i) + '.setText(self.needs[i - 1])')
            eval('self.pushProduct_' + str(i) + '.show()')

    def hide_products(self):
        for i in range(1, 8):
            eval('self.pushProduct_' + str(i) + '.hide()')

    def add_count(self, btn):
        global prog, choose

        choose = btn.text()
        prog.dialogWin.show()  # Запуск окна старта


class StatisticWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('statistic.ui', self)

        self.pushBackFromStatistic.clicked.connect(lambda: back_to_main(self))

        self.chooseBox.addItem('Белки')
        self.chooseBox.addItem('Жиры')
        self.chooseBox.addItem('Углеводы')
        self.chooseBox.addItem('Ккал')

        self.pushBuild.clicked.connect(lambda: self.edit_graphic(self.chooseBox.currentText()))

    def edit_graphic(self, choose):
        stat = self.get_days_stat()
        # stat = {'12.06.18': [50, 70, 100, 90], '13.07.18': [60, 150, 10, 20]}
        print(stat)

        if choose == 'Белки':
            x, y = dict(enumerate([date for date in stat])), [stat[date][0] for date in stat]
        elif choose == 'Жиры':
            x, y = dict(enumerate([date for date in stat])), [stat[date][1] for date in stat]
        elif choose == 'Углеводы':
            x, y = dict(enumerate([date for date in stat])), [stat[date][2] for date in stat]
        else:
            x, y = dict(enumerate([date for date in stat])), [stat[date][3] for date in stat]

        stringaxis = pyqtgraph.AxisItem(orientation='bottom')
        stringaxis.setTicks([x.items()])
        plot = pyqtgraph.PlotWidget(self, axisItems={'bottom': stringaxis})
        plot.plot(list(x.keys()), y, pen='b')

        plot.move(330, 20)
        plot.resize(441, 381)
        plot.show()

    def get_days_stat(self):
        stat = {}
        with open('DATABASE.txt') as file:
            for line in file.readlines():
                date, value = line[4: line.find(':') - 1].replace('-', '.'), eval(line[line.find(':') + 2: -2])
                if date not in stat:
                    stat[date] = value
                else:
                    for i in range(4):
                        stat[date][i] += value[i]
        return stat


class ProgramInformation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('program_info.ui', self)

        self.pushBackFromInfo.clicked.connect(lambda: back_to_main(self))


class DialogCount(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 210)
        self.initUI()
        self.setWindowIcon(QIcon(QPixmap('icon.png')))

        self.spinBox.setValue(100)

    def initUI(self):
        uic.loadUi('dialog_count.ui', self)

        self.pushOkCount.clicked.connect(self.run)

    def run(self):
        g = float(self.spinBox.value()) / 100
        self.hide()
        prog.resultWin.initUI(g)
        prog.resultWin.show()


class Result(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 210)
        uic.loadUi('result.ui', self)
        self.setWindowIcon(QIcon(QPixmap('icon.png')))

    def initUI(self, g):
        global choose

        print(g)
        fats = float(str(round(float(PRODUCTS_DICT[choose][0]) * g, 2)))
        proteins = float(str(round(float(PRODUCTS_DICT[choose][1]) * g, 2)))
        carbohydrates = float(str(round(float(PRODUCTS_DICT[choose][2]) * g, 2)))
        calories = float(str(round(float(PRODUCTS_DICT[choose][3]) * g, 2)))
        self.label_1.setText('Жиры: ' + str(fats))
        self.label_2.setText('Белки: ' + str(proteins))
        self.label_3.setText('Углеводы: ' + str(carbohydrates))
        self.label_4.setText('Ккал: ' + str(calories))
        date = str(datetime.datetime.now())[:10]
        if date not in HISTORY:
            HISTORY[date] = [fats, proteins, carbohydrates, calories]
        else:
            HISTORY[date][0] += fats
            HISTORY[date][1] += proteins
            HISTORY[date][2] += carbohydrates
            HISTORY[date][3] += calories
        with open('DATABASE.txt', 'a') as db:
            db.write(str(HISTORY) + '\n')
        print(HISTORY)
        self.pushOkResult.clicked.connect(self.hide)


def connect():
    """ Connect to MySQL database """
    try:
        dict_products = {}
        conn = sqlite3.connect("products.db")  # или :memory: чтобы сохранить в RAM

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products2")

        row = cursor.fetchall()

        for elem in row:
            dict_products[elem[0].lower()] = [elem[1], elem[2], elem[3], elem[4]]

        return dict_products


    except Exception as e:
        return e

    finally:
        conn.close()


# Функция на замену спец символов
def clearWord(word):
    return re.sub('[' + string.punctuation + ']', '', word)


def set_background(self):  # Установка фона для окон
    self.setWindowIcon(QIcon(QPixmap('icon.png')))

    self.bg = QLabel(self)
    self.bg.resize(900, 600)
    self.bg.setPixmap(QPixmap("image.jpg").scaled(900, 600))


def back_to_main(self):  # Back to main window button
    global prog

    prog.mainWin.show()  # Запуск окна старта
    self.hide()


def send_email():
    # Настройки
    mail_sender = 'biostat18@mail.ru'
    mail_receiver = 'biostat18@mail.ru'
    username = 'biostat18@mail.ru'
    password = 'qwerty3301'
    server = smtplib.SMTP('smtp.mail.ru:587')

    # Формируем тело письма
    subject = 'We have a new informations'
    body = HISTORY
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # Отпавляем письмо
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(mail_sender, mail_receiver, msg.as_string())
    server.quit()


pyqtgraph.setConfigOption('background', QColor(244, 244, 244))
pyqtgraph.setConfigOption('foreground', QColor(0, 0, 0))

HISTORY = {}
PRODUCTS_DICT = connect()
app = QApplication(sys.argv)
prog = BioStat()
sys.exit(app.exec_())
