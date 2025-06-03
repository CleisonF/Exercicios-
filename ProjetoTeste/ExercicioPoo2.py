class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Olá meu nome é {self.nome} e tenho {self.idade} anos.'

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_aluno(self):
        print(f'Alunos do curso {self.nome}:')
        for aluno in self.alunos:
            print(f'- {aluno.nome}')

c1 = Aluno('Maria', 4)
print(c1.apresentar())
