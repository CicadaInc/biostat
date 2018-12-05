import sys
import sqlite3
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
        if text.lower() in PRODUCTS_DICT:
            print('yes')


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
