import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


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

    def searching(self):  # Search button
        pass


class StatisticWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('statistic.ui', self)

        self.pushBackFromStatistic.clicked.connect(lambda: back_to_main(self))


class ProgramInformation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('program_info.ui', self)

        self.pushBackFromInfo.clicked.connect(lambda: back_to_main(self))


def set_background(self):  # Установка фона для окон
    self.bg = QLabel(self)
    self.bg.resize(900, 600)
    self.bg.setPixmap(QPixmap("image.jpg").scaled(900, 600))


def back_to_main(self):  # Back to main window button
    global prog

    prog.mainWin.show()  # Запуск окна старта
    self.hide()


app = QApplication(sys.argv)
prog = BioStat()
sys.exit(app.exec_())
