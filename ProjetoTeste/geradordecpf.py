"""
10  9  8  7  6  5  4  3  2
0  7   2  8  9  5  9  3  5
0  63  16 56 54 25 36 9  10

269 * 10 = 2690
2690 % 11 = 6
"""
# gerador de cpf
import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador = 10
resultado = 0
for digito in nove_digitos:
    resultado += (int(digito) * contador)
    contador -=1


digito1 = (resultado * 10 % 11)
digito1 = digito1 if digito1 <= 9 else 0

dez_digitos = nove_digitos + str(digito1)
contador2 = 11

resultado2 = 0
for digito in dez_digitos:
    resultado2 += (int(digito) * contador2)
    contador2 -=1
digito2 = (resultado2 * 10 % 11)
digito2 = digito2 if digito2 <= 9 else 0
novo_cpf = f'{nove_digitos}{digito1}{digito2}'
print(novo_cpf)