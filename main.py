import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


# Main class
class BioStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWin = MainMenu()
        self.hide()

    def starting(self):
        self.startWin = StartWindow()


# Main menu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()

    def init_UI(self):
        # Установка фона
        set_fone(self)

        # Загрузка GUI
        uic.loadUi('main.ui', self)

        # Подкличение функционала к кнопкам
        self.pushStart.clicked.connect(self.starting)

    def starting(self):
        global prog

        BioStat.starting(prog)  # Запуск окна старта из основного класса
        self.hide()


# Window start
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()

    def init_UI(self):
        # Установка фона
        set_fone(self)

        # Загрузка GUI
        uic.loadUi('start.ui', self)

    def searching(self):  # Search button
        pass

    def backToMain(self):  # Back to main window button
        pass


def set_fone(self):  # Установка фона для окон
    self.fone = QLabel(self)
    self.fone.resize(900, 600)
    self.fone.move(0, 0)
    self.fone.setPixmap(QPixmap("image.jpg").scaled(901, 600))


app = QApplication(sys.argv)
prog = BioStat()
sys.exit(app.exec_())