from datetime import datetime

ANO_ATUAL = datetime.now().year

class Pessoa:
    at = 'Valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return ANO_ATUAL - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(vars(p1))