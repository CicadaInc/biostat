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


# Main menu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
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

        prog.startWin.show()  # Запуск окна старта
        self.hide()


# Window start
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        # Установка фона
        set_fone(self)

        # Загрузка GUI
        uic.loadUi('start.ui', self)

        self.pushBack.clicked.connect(self.back_to_main)

    def searching(self):  # Search button
        pass

    def back_to_main(self):  # Back to main window button
        global prog

        prog.mainWin.show()  # Запуск окна старта
        self.hide()


def set_fone(self):  # Установка фона для окон
    self.fone = QLabel(self)
    self.fone.resize(900, 600)
    self.fone.move(0, 0)
    self.fone.setPixmap(QPixmap("image.jpg").scaled(901, 600))


app = QApplication(sys.argv)
prog = BioStat()
sys.exit(app.exec_())
