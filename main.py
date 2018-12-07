import sys
import sqlite3
import re
import string
import Stemmer
import numpy as np
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


# Main class
class BioStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWin = MainMenu()
        self.startWin = StartWindow()
        self.statisticWin = StatisticWindow()
        self.progInfo = ProgramInformation()


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
        self.button_design(self.pushStart)
        self.button_design(self.pushStatistic)
        self.button_design(self.pushAbout)
        self.button_design(self.pushClean)

    def button_design(self, button):
        button.setStyleSheet('QPushButton {font: 13pt "verdana"; '
                             'background-color: rgb(255, 255, 255); '
                             'border-radius: 2px; '
                             'border: 2px solid #9a9; '
                             'box-shadow: 4px 4px 4px rgba(8, 8, 8, 0.5)} '
                             'QPushButton:hover {background-color: rgba(231, 253, 255, 0.7); border: 2px solid #9a9;}')

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

        self.pushBackFromStart.clicked.connect(lambda: back_to_main(self))
        self.button_design(self.pushBackFromStart)
        self.pushOkSearch.clicked.connect(self.searching)
        self.button_design(self.pushOkSearch)

    def button_design(self, button):
        button.setStyleSheet('QPushButton {font: 13pt "verdana"; '
                             'background-color: rgb(255, 255, 255); '
                             'border-radius: 2px; '
                             'border: 2px solid #9a9; '
                             'box-shadow: 4px 4px 4px rgba(8, 8, 8, 0.5)} '
                             'QPushButton:hover {background-color: rgba(231, 253, 255, 0.7); border: 2px solid #9a9;}')

    def searching(self):  # Search button
        text = self.textSearch.toPlainText()
        needs = []
        for item in PRODUCTS_DICT:
            if clearWord(text.lower()) in item:
                needs.append(item)
        print(needs)

        # Почему-то кнопка не создаётся
        for i in range(len(needs)):
            self.pushProduct_1 = QPushButton(needs[i], self)
            self.pushProduct_1.resize(301, 21)
            self.pushProduct_1.move(470, 100)
            self.button_design(self.pushProduct_1)
        # if clearWord(text.lower()) in PRODUCTS_DICT:
        #     print('yes')
        # else:
        #     print('no')
        # # ------------------
        #
        # lsa = LSA()
        # docs = [text]
        # docs += PRODUCTS_DICT.keys()
        #
        # docs_copy = docs.copy()
        #
        # for i in range(len(docs)):
        #     lsa.add_sentence(docs[i])
        #
        # for i in range(len(docs)):
        #     docs[i] = lsa.stop_symbols(docs[i])
        #
        # for i in range(len(docs)):
        #     docs[i] = lsa.my_stemmer(docs[i])
        #
        # similar_words = sorted(lsa.search_common_words(docs))
        #
        # matrix = lsa.drawing_up_the_matrix(similar_words, docs)
        #
        # if matrix != []:
        #     U, S, Vt = np.linalg.svd(matrix)
        #
        #     coord = -1 * Vt[0:2, :]
        #     new_coord = []
        #
        #     for i in range(len(docs)):
        #         new_coord.append((round(coord[0][i], 3), round(coord[1][i], 3)))
        #
        #     # print(new_coord)
        #     print(docs_copy[lsa.find_near(new_coord[0], new_coord[1:])])
        # else:
        #     print('К сожалению, ничего не найдено.')
        #
        # # ------------------


class StatisticWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('statistic.ui', self)

        self.pushBackFromStatistic.clicked.connect(lambda: back_to_main(self))
        self.button_design(self.pushBackFromStatistic)

    def button_design(self, button):
        button.setStyleSheet('QPushButton {font: 13pt "verdana"; '
                             'background-color: rgb(255, 255, 255); '
                             'border-radius: 2px; '
                             'border: 2px solid #9a9; '
                             'box-shadow: 4px 4px 4px rgba(8, 8, 8, 0.5)} '
                             'QPushButton:hover {background-color: rgba(231, 253, 255, 0.7); border: 2px solid #9a9;}')


class ProgramInformation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('program_info.ui', self)

        self.pushBackFromInfo.clicked.connect(lambda: back_to_main(self))
        self.button_design(self.pushBackFromInfo)

    def button_design(self, button):
        button.setStyleSheet('QPushButton {font: 13pt "verdana"; '
                             'background-color: rgb(255, 255, 255); '
                             'border-radius: 2px; '
                             'border: 2px solid #9a9; '
                             'box-shadow: 4px 4px 4px rgba(8, 8, 8, 0.5)} '
                             'QPushButton:hover {background-color: rgba(231, 253, 255, 0.7); border: 2px solid #9a9;}')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Результат')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("ОК")
        self.button_1.clicked.connect(self.run)

        self.show()

    def run(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите имя", "Как тебя зовут?"
        )
        if okBtnPressed:
            self.button_1.setText(i)


class LSA:
    def __init__(self):
        self.docs = []

    # Проверка на существование матрицы
    def check_matrix(self, matrix):
        if matrix == [] or matrix[0] == []:
            return False
        else:
            return True

    # Добавить предложение
    def add_sentence(self, sentence):
        self.docs.append(sentence)

    # Удаление стоп-символов
    def stop_symbols(self, sentence):
        stop = ['-', 'еще', 'него', 'сказать', 'а', 'ж', 'нее', 'со', 'без', 'же', 'ней', 'совсем', 'более', 'жизнь',
                'нельзя', 'так', 'больше', 'за', 'нет', 'такой', 'будет', 'зачем', 'ни', 'там', 'будто', 'здесь',
                'нибудь',
                'тебя', 'бы', 'и', 'никогда', 'тем', 'был', 'из', 'ним', 'теперь', 'была', 'из-за', 'них', 'то', 'были',
                'или', 'ничего', 'тогда', 'было', 'им', 'но', 'того', 'быть', 'иногда', 'ну', 'тоже', 'в', 'их', 'о',
                'только', 'вам', 'к', 'об', 'том', 'вас', 'кажется', 'один', 'тот', 'вдруг', 'как', 'он', 'три', 'ведь',
                'какая', 'она', 'тут', 'во', 'какой', 'они', 'ты', 'вот', 'когда', 'опять', 'у', 'впрочем', 'конечно',
                'от',
                'уж', 'все', 'которого', 'перед', 'уже', 'всегда', 'которые', 'по', 'хорошо', 'всего', 'кто', 'под',
                'хоть',
                'всех', 'куда', 'после', 'чего', 'всю', 'ли', 'потом', 'человек', 'вы', 'лучше', 'потому', 'чем', 'г',
                'между', 'почти', 'через', 'где', 'меня', 'при', 'что', 'говорил', 'мне', 'про', 'чтоб', 'да', 'много',
                'раз', 'чтобы', 'даже', 'может', 'разве', 'чуть', 'два', 'можно', 'с', 'эти', 'для', 'мой', 'сам',
                'этого',
                'до', 'моя', 'свое', 'этой', 'другой', 'мы', 'свою', 'этом', 'его', 'на', 'себе', 'этот', 'ее', 'над',
                'себя', 'эту', 'ей', 'надо', 'сегодня', 'я', 'ему', 'наконец', 'сейчас', 'если', 'нас', 'сказал',
                'есть',
                'не', 'сказала']

        sentence = clearWord(sentence).lower().split()
        clear_sentence = ''
        for word in sentence:
            if word not in stop:
                clear_sentence += word + ' '
        return clear_sentence.strip()

    # Получает предложение и выдаёт это предложение, состоящее из основ слов
    def my_stemmer(self, sentence):
        stemmer = Stemmer.Stemmer('russian')
        ready = ''
        sentence = sentence.split()
        for word in sentence:
            word = stemmer.stemWord(word)
            ready += word + ' '
        return ready.strip()

    # Поиск общих слов
    def search_common_words(self, lst):
        result = []
        slov = {}
        for i in range(len(lst)):
            words = lst[i].split()
            for word in words:
                if word not in slov:
                    slov[word] = 1
                else:
                    slov[word] += 1
        keys = list(slov.keys())
        values = list(slov.values())
        for i in range(len(values)):
            if values[i] > 1 and keys[i] not in result:
                result.append(keys[i])
        return result

    # Составление матрицы
    def drawing_up_the_matrix(self, words, sentences):
        matrix = []
        for i in range(len(words)):
            matrix.append([])
            for text in sentences:
                text = text.split()
                matrix[i].append(text.count(words[i]))
        return matrix

    # Поиск ближайшего предложения
    def find_near(self, coord, other_coords):
        values = []
        for i in range(len(other_coords)):
            if round(abs(coord[0] - other_coords[i][0]), 4) >= 0.1 or round(abs(coord[1] - other_coords[i][1]),
                                                                            4) >= 0.1:
                values.append(
                    (round(abs(coord[0] - other_coords[i][0]), 4), round(abs(coord[1] - other_coords[i][1]), 4)))
        return other_coords.index(other_coords[values.index(min(values))]) + 1


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


PRODUCTS_DICT = connect()
app = QApplication(sys.argv)
prog = BioStat()
sys.exit(app.exec_())
