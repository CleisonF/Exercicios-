
class Carro:
    def __init__(self, marca, modelo, idade):
        self.marca = marca
        self.modelo = modelo
        self.idade = idade

    def exibir_info(self):
        return f'Esse carro é da marca {self.marca} {self.modelo} do ano {self.idade}'


    def eh_antigo(self):
        if self.idade <= 2010:
            return f'Seu carro do ano de {self.idade} é um carro antigo.'
        else:
            return f'Seu Carro do ano de {self.idade} é um carro novo.'


c1 = Carro('Toyota', 'Corolla', 2009)
print(c1.exibir_info())
print((c1.eh_antigo()))