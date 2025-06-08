import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow

app = QApplication(sys.argv)
windon = QMainWindow()
central_widget = QWidget()
windon.setCentralWidget(central_widget)
windon.setWindowTitle('Minha janela')

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red;')


botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)
layout.addWidget(botao2)
def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')

#statusBar
status_bar = windon.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

#menuBar
menu = windon.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))


windon.show()

app.exec()
