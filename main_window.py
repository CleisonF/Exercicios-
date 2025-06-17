from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs ) -> None:
        super().__init__(parent, *args, **kwargs)

        #configurando o layout básico
        self.cw = QWidget()
        self.vlayout = QVBoxLayout()
        self.cw.setLayout(self.vlayout)
        self.setCentralWidget(self.cw)

        #titulo da janela
        self.setWindowTitle('Calculadora')


        #ultima coisa a ser feita
    def AdjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(),self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vlayout.addWidget(widget)
