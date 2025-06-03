from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
       return f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':
    p1 = Pessoa(nome='Luiz',sobrenome= 'Roberto')
    p2 = Pessoa(nome='Maria', sobrenome= 'Helena')
    print(p1)
    print(p1.nome_completo)
    print(p2.nome_completo)
    print(p2)


