import math
from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpyt, isValidNumber, convertToNumber
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow



class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info',window:'MainWindow' ,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N' , '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)


    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertButtonText)
        self.display.operetorPressed.connect(self._configLeftOp)

        for row_number, row in enumerate(self._gridMask):
            for column_number, buttonText in enumerate(row):
                button = Button(buttonText)
                if not isNumOrDot(buttonText) and not isEmpyt(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertButtonText, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == 'D':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-/*':
            self._connectButtonClicked(button, self._makeSlot(self._configLeftOp, text))

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs ):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))


    def _insertButtonText(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
               return
        self.display.insert(text)
        self.display.setFocus()


    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()


    def _configLeftOp(self, text):
        displayText = self.display.text() # Numero dá esquerda (left)
        self.display.clear() #limpa o display
        self.display.setFocus()

        # Se a pessoa clico no operador sem configurar qualquer numero antes
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return

        # Se houver algo no número da esquerda, não fazemos nada. Aguardaremos o númedo da direita.
        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'


    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Conta incompleta.')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'error':
            self._left = None

    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgbox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
