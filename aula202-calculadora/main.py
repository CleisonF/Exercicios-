import sys

from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from display import Display
from styles import ButtonsGrid

if __name__ == '__main__':
    #Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    info = Info('')
    window.addWidgetToVLayout(info)

    #Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    display = Display()
    window.addWidgetToVLayout(display)

    #grid
    buttonsgrid = ButtonsGrid(display, info, window)
    window.vlayout.addLayout(buttonsgrid)

    #buttons

    #executa tudo
    window.show()
    app.exec()
