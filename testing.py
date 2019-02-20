class StatisticWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.init_UI()

    def init_UI(self):
        set_background(self)

        uic.loadUi('statistic.ui', self)

        self.pushBackFromStatistic.clicked.connect(lambda: back_to_main(self))

        self.chooseBox.addItem('Белки')
        self.chooseBox.addItem('Жиры')
        self.chooseBox.addItem('Углеводы')
        self.chooseBox.addItem('Ккал')

        self.pushBuild.clicked.connect(lambda: self.edit_graphic(self.chooseBox.currentText()))

    def edit_graphic(self, choose):
        print(choose)
        if choose == 'Белки':
            self.graph.plot([i for i in range(10)], [i for i in range(10)], pen='b')
        elif choose == 'Жиры':
            self.graph.plot([i for i in range(10)], [i for i in range(10)], pen='b')
        elif choose == 'Углеводы':
            self.graph.plot([i for i in range(10)], [i for i in range(10)], pen='b')
        else:
            self.graph.plot([i for i in range(10)], [i for i in range(10)], pen='b')


pyqtgraph.setConfigOption('background', QColor(244, 244, 244))
pyqtgraph.setConfigOption('foreground', QColor(0, 0, 0))
