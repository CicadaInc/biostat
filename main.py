import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

'''Основной класс (от него идут все окна программы)'''


class BioStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWin = MainMenu()
        self.hide()

    def starting(self):
        self.startWin = StartWindow()


'''Основное меню'''


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()

    def init_UI(self):
        set_fone(self)

        uic.loadUi('main.ui', self)

        self.pushStart.clicked.connect(self.starting)
        self.pushStatistic.clicked.connect(self.stat)

    def starting(self):
        global prog

        BioStat.starting(prog)  # Запуск окна старта из основного класса
        self.hide()

    def stat(self):
        pass


'''Окно при нажатии на старт'''


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()

    def init_UI(self):
        set_fone(self)

        uic.loadUi('main.ui', self)


def set_fone(self):  # Установка фона для окон
    self.fone = QLabel(self)
    self.fone.resize(900, 600)
    self.fone.move(0, 0)
    self.fone.setPixmap(QPixmap("image.jpg").scaled(901, 600))


app = QApplication(sys.argv)
prog = BioStat()
sys.exit(app.exec_())
