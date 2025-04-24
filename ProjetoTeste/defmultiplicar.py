#def duplicar(numero):
#    return numero * 2


#print(duplicar(2))


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
tripliar = criar_multiplicador(3)

print(duplicar(2))
print(tripliar(2))
