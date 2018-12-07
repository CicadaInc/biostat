import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Добавляем фон
        self.fone = QLabel(self)
        self.fone.resize(800, 500)
        self.fone.move(0, 0)
        self.fone.setPixmap(QPixmap("image.jpg").scaled(800, 500))

        # Загрузка GUI
        uic.loadUi('main.ui', self)

        # Подкличение функционала к кнопкам
        self.pushStart.clicked.connect(self.starting)

    def starting(self):  # Start button
        global window
        window = WindowStart()
        window.show()


class WindowStart(QMainWindow):
    def __init__(self):
        super().__init__()

        # Добавляем фон
        self.fone = QLabel(self)
        self.fone.resize(800, 500)
        self.fone.move(0, 0)
        self.fone.setPixmap(QPixmap("image.jpg").scaled(800, 500))

        # Загрузка GUI
        uic.loadUi('start.ui', self)

        # Подкличение функционала к кнопкам
        self.pushOkSearch.clicked.connect(self.searching)
        self.pushBack.clicked.connect(self.backToMain)

    def searching(self):  # Search button
        pass

    def backToMain(self):  # Back to main window button
        pass


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
