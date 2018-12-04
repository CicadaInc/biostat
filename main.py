import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fone = QLabel(self)
        self.fone.resize(800, 500)
        self.fone.move(0, 0)
        self.fone.setPixmap(QPixmap("image.jpg").scaled(800, 500))

        uic.loadUi('main.ui', self)

        self.pushStart.clicked.connect(self.starting)
        self.pushStatistic.clicked.connect(self.stat)

        self.lbl = QLabel(self)
        self.lbl.resize(300, 300)

    def starting(self):
        #self.window = MyWidget1()
        #self.window.show()
        self.pushStart.hide()

    def stat(self):
        self.lbl.setText('ldpawlfpawlfpawga')


class MyWidget1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
