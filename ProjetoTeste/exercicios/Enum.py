import enum



Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', 'ACIMA', 'ABAIXO'])


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção invalida')

    print(f'Movendo para a {direcao.name}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)