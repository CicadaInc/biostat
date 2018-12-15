import sys
import sqlite3
import re
import string
import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QApplication
import pyqtgraph


# Main menu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        # Установка фона
        set_background(self)

        # Загрузка GUI
        uic.loadUi('main.ui', self)

        # Подкличение функционала к кнопкам
        self.pushStart.clicked.connect(lambda: show_window(self, startWin))
        self.pushStatistic.clicked.connect(
            lambda: (show_window(self, statisticWin), statisticWin.set_pfc_information()))
        self.pushAbout.clicked.connect(lambda: show_window(self, progInfo))
        self.pushAdvices.clicked.connect(
            lambda: (show_window(self, adviceWin), adviceWin.set_pfc_inforamtion()))
        self.pushClean.clicked.connect(self.clean_progress)
        self.pushExit.clicked.connect(self.close)

    def clean_progress(self):
        global statisticWin, startWin, mainWin
        global dialogWin, dialogWin2, adviceWin

        HISTORY.clear()

        with open('DATABASE.txt', 'w') as db:
            db.write('')
        with open('user_data.txt', 'w') as db:
            db.write('')

        startWin = StartWindow()
        statisticWin = StatisticWindow()
        dialogWin2 = StartQuestions()
        adviceWin = AdviceWindow()

        mainWin.hide()


class AdviceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.proteinDisInf, self.fatDisInf, \
        self.ch_diseasesDisInf, self.Kkal_diseasesDisInf = '', '', '', ''

        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi("advices.ui", self)

        self.pushBackFromAdvices.clicked.connect(lambda: show_window(self, mainWin))

        self.pushCalculate.clicked.connect(self.calculate_normal)

        self.pushProteinDiseases.clicked.connect(
            lambda: (diseasesWin.inf.setText(self.proteinDisInf),
                     show_window(None, diseasesWin)))
        self.pushFatDiseases.clicked.connect(
            lambda: (diseasesWin.inf.setText(self.fatDisInf),
                     show_window(None, diseasesWin)))
        self.pushCarbohydrateDiseases.clicked.connect(
            lambda: (diseasesWin.inf.setText(self.ch_diseasesDisInf),
                     show_window(None, diseasesWin)))
        self.pushKkalDiseases.clicked.connect(
            lambda: (diseasesWin.inf.setText(self.Kkal_diseasesDisInf),
                     show_window(None, diseasesWin)))

        self.proteins_2.hide()
        self.fats_2.hide()
        self.carbohydrates_2.hide()
        self.Kkal_2.hide()
        self.pushProteinDiseases.hide()
        self.pushFatDiseases.hide()
        self.pushCarbohydrateDiseases.hide()
        self.pushKkalDiseases.hide()

    def set_pfc_inforamtion(self):
        with open("DATABASE.txt") as file:
            self.data, days = [0, 0, 0, 0], 0
            for line in file.readlines()[-7:]:
                value = eval(line[line.find(':') + 2: -2])
                self.data = [self.data[i] + value[i] for i in range(4)]
                days += 1

        try:
            self.data = list(map(lambda el: round(el / days, 2), self.data))
        except ZeroDivisionError:
            pass
        self.proteins.setText(str(self.data[0]) + ' г белков')
        self.fats.setText(str(self.data[1]) + ' г жиров')
        self.carbohydrates.setText(str(self.data[2]) + ' г углеводов')
        self.Kkal.setText(str(self.data[3]) + ' Ккал')

    def calculate_normal(self):
        with open("user_data.txt", encoding='utf-8') as file:
            age, weight, height, gender = map(lambda el: el[:-1], file.readlines())
            age, weight, height = int(age), int(weight), int(height)
            choice = self.chooseActivity.currentText()

        if gender == 'Мужчина':
            wk, pk, hk, ak = 13.397, 88.362, 4.799, 5.677
            p, f, ch = 3, 2, 5
        else:
            wk, pk, hk, ak = 9.247, 447.593, 3.098, 4.330
            p, f, ch = 2.2, 2, 4.5

        if choice == 'Сидячий образ жизни':
            amr = 1.2
        elif choice == 'Умеренная активность':
            amr = 1.375
        elif choice == 'Средняя активность':
            amr = 1.55
        elif choice == 'Интенсивные нагрузки':
            amr = 1.725
        elif choice == 'Для спортсменов':
            amr = 1.9
        elif choice == 'Для увеличения массы':
            amr = 1.2
        else:
            amr = 0.8

        bmr = pk + wk * weight + hk * height - ak * age
        bmr *= amr

        part = bmr / (p + f + ch)
        p *= part
        f *= part
        ch *= part

        self.proteins_2.setText(str(int(round(p, -1))) + ' г белков')
        self.fats_2.setText(str(int(round(f, -1))) + ' г жиров')
        self.carbohydrates_2.setText(str(int(round(ch, -1))) + ' г углеводов')
        self.Kkal_2.setText(str(int(round(bmr, -1))) + ' Ккал')

        self.get_advice(self.data, [p, f, ch, bmr])

        self.proteins_2.show()
        self.fats_2.show()
        self.carbohydrates_2.show()
        self.Kkal_2.show()

    def get_advice(self, consume, normal):
        if abs(consume[0] - normal[0]) > 100:
            if consume[0] - normal[0] < -100:
                self.protein_advice.setText('Нужно увеличить кол-во потребляемых белков')
                self.proteinDisInf = 'Приводит к гипотонии,\n' \
                                     'дистрофии мышц,\n' \
                                     'снижению тургора тканей,\n' \
                                     'проблемам с сердцем,\n' \
                                     'печенью, памятью,\n' \
                                     'гормонами и иммунитетом'
            elif consume[0] - normal[0] > 100:
                self.protein_advice.setText('Нужно уменьшить кол-во потребляемых белков')
                self.proteinDisInf = 'Приводит к ожирению,\n' \
                                     'создает доп. нагрузку на почки,\n' \
                                     'способствует выщелачиванию\n' \
                                     'минералов из костной ткани'
            self.pushProteinDiseases.show()
        else:
            self.protein_advice.setText('Кол-во потребляемых белков в порядке')

        if abs(consume[1] - normal[1]) > 100:
            if consume[1] - normal[1] < -100:
                self.fat_advice.setText('Нужно увеличить кол-во потребляемых жиров')
                self.fatDisInf = 'Приводит к сухости кожи,\n слабости, обезвоживанию,\n' \
                                 'депрессии\n' \
                                 'Ощущению голода и холода\n' \
                                 'ухудшению зрения,\n концентрации, памяти и\n' \
                                 'сердечно-сосудистой системы'
            elif consume[1] - normal[1] > 100:
                self.fat_advice.setText('Нужно уменьшить кол-во потребляемых жиров')
                self.fatDisInf = 'Приводит к атеросклерозу,\n' \
                                 'ишемической болезни сердца,\n' \
                                 'ожирению, желчнокаменной болезни,\n' \
                                 'ухудшает усвоение белков, кальция, магния'
            self.pushFatDiseases.show()
        else:
            self.fat_advice.setText('Кол-во потребляемых жиров в порядке')

        if abs(consume[2] - normal[2]) > 100:
            if consume[2] - normal[2] < -100:
                self.carbohydrate_advice.setText('Нужно увеличить кол-во потребляемых углеводов')
                self.ch_diseasesDisInf = 'Приводит к слабости,\n' \
                                         'сонливости,\n' \
                                         'головокружению, головной боли\n' \
                                         'Чувству голода, тошноте,\n' \
                                         'потливости, дрожи рук'
            elif consume[2] - normal[2] > 100:
                self.carbohydrate_advice.setText('Нужно уменьшить кол-во потребляемых углеводов')
                self.ch_diseasesDisInf = 'Приводит к ожирению,\n' \
                                         'сахарному диабету,\n' \
                                         'гипергликемии,\n' \
                                         'сердечно-сосудистым\n' \
                                         'заболеваниям'
            self.pushCarbohydrateDiseases.show()
        else:
            self.carbohydrate_advice.setText('Кол-во потребляемых углеводов в порядке')

        if abs(consume[3] - normal[3]) > 100:
            if consume[3] - normal[3] < -100:
                self.Kkal_advice.setText('Нужно увеличить кол-во потребляемых калорий')
                self.Kkal_diseasesDisInf = 'Приводит к усталости,\n' \
                                           'избыточному похудению\n' \
                                           '(см. выбранный образ жизни)'
            elif consume[3] - normal[3] > 100:
                self.Kkal_advice.setText('Нужно уменьшить кол-во потребляемых калорий')
                self.Kkal_diseasesDisInf = 'Приводит к избыточному весу\n' \
                                           '(см. выбранный образ жизни)'
            self.pushKkalDiseases.show()
        else:
            self.Kkal_advice.setText('Кол-во потребляемых калорий в порядке')


class Diseases(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        uic.loadUi("diseases.ui", self)

        self.pushOkDiseases.clicked.connect(lambda: show_window(self, None))


class StartQuestions(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        uic.loadUi("start_quests.ui", self)

        self.pushOkQuests.clicked.connect(self.save_data)

        with open("user_data.txt") as file:
            if file.readlines():
                show_window(self, mainWin)
            else:
                self.show()

    def save_data(self):
        with open("user_data.txt", mode='w', encoding='utf-8') as file:
            file.write(self.ageInput.text() + '\n')
            file.write(self.weightInput.text() + '\n')
            file.write(self.heightInput.text() + '\n')
            file.write(self.genderChoice.currentText() + '\n')
        show_window(self, mainWin)


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

        self.pushBackFromStart.clicked.connect(lambda: show_window(self, mainWin))
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
        global choose

        choose = btn.text()
        show_window(None, dialogWin)  # Запуск окна старта


class StatisticWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('statistic.ui', self)

        self.pushBackFromStatistic.clicked.connect(lambda: show_window(self, mainWin))

        self.pushBuild.clicked.connect(lambda: self.edit_graphic(self.chooseBox.currentText()))

        self.zero_plot = pyqtgraph.PlotWidget(self)
        self.zero_plot.move(380, 50)
        self.zero_plot.resize(300, 330)
        self.zero_plot.show()

    def set_pfc_information(self):
        with open("DATABASE.txt") as file:
            data, days = [0, 0, 0, 0], 0
            for line in file.readlines()[-7:]:
                value = eval(line[line.find(':') + 2: -2])
                data = [data[i] + value[i] for i in range(4)]
                days += 1

        try:
            data = list(map(lambda el: round(el / days, 2), data))
        except ZeroDivisionError:
            pass
        self.proteins.setText(str(data[0]) + ' г белков')
        self.fats.setText(str(data[1]) + ' г жиров')
        self.carbohydrates.setText(str(data[2]) + ' г углеводов')
        self.Kkal.setText(str(data[3]) + ' Ккал')

    def edit_graphic(self, choose):
        stat = self.get_days_stat()
        print(stat)
        step = len(stat) // 6 + 1

        if choose == 'Белки':
            x, y = dict(enumerate([list(stat.keys())[i] for i in range(0, len(stat), step)])), \
                   [stat[list(stat.keys())[i]][0] for i in range(0, len(stat), step)]
        elif choose == 'Жиры':
            x, y = dict(enumerate([list(stat.keys())[i] for i in range(0, len(stat), step)])), \
                   [stat[list(stat.keys())[i]][1] for i in range(0, len(stat), step)]
        elif choose == 'Углеводы':
            x, y = dict(enumerate([list(stat.keys())[i] for i in range(0, len(stat), step)])), \
                   [stat[list(stat.keys())[i]][2] for i in range(0, len(stat), step)]
        else:
            x, y = dict(enumerate([list(stat.keys())[i] for i in range(0, len(stat), step)])), \
                   [stat[list(stat.keys())[i]][3] for i in range(0, len(stat), step)]

        stringaxis = pyqtgraph.AxisItem(orientation='bottom')
        stringaxis.setTicks([x.items()])
        self.plot = pyqtgraph.PlotWidget(self, axisItems={'bottom': stringaxis})
        self.plot.plot(list(x.keys()), y, pen='b')

        self.zero_plot.hide()

        self.plot.move(380, 50)
        self.plot.resize(300, 330)
        self.plot.show()

    def get_days_stat(self):
        stat = {}
        with open('DATABASE.txt') as file:
            for line in file.readlines():
                date, value = line[4: line.find(':') - 1].replace('-', '.'), eval(
                    line[line.find(':') + 2: -2])
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

        self.pushBackFromInfo.clicked.connect(lambda: show_window(self, mainWin))


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
        resultWin.initUI(g)
        show_window(self, resultWin)


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
            HISTORY.clear()
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


def show_window(old, new):
    if not (new is None):
        new.show()
    if not (old is None):
        old.hide()


pyqtgraph.setConfigOption('background', QColor(244, 244, 244))
pyqtgraph.setConfigOption('foreground', QColor(0, 0, 0))

HISTORY = {}
PRODUCTS_DICT = connect()
app = QApplication(sys.argv)

mainWin = MainMenu()
startWin = StartWindow()
statisticWin = StatisticWindow()
progInfo = ProgramInformation()
dialogWin = DialogCount()
dialogWin2 = StartQuestions()
diseasesWin = Diseases()
adviceWin = AdviceWindow()
resultWin = Result()

sys.exit(app.exec_())
