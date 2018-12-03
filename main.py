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
        self.pushButton.clicked.connect(self.run)

    def run(self):
        pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
