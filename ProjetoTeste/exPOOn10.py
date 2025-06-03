class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante


    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca =  Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1 = Motor('1.0')
fusca._fabricante = volkswagen
fusca._motor = motor_1
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

celta = Carro('Celta')
Chevrolet = Fabricante('Chevrolet')
motor_2 = Motor('1.4')
celta._fabricante = Chevrolet
celta._motor = motor_2
print(celta.nome, celta.fabricante.nome, celta.motor.nome)
