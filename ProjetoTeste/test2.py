"""from testeprojeto.lib.interface import leiaInt
numero =  leiaInt('Digite um número: ')

if numero % 2 == 0:
    print(f'O numero que você digitou é {numero} e ele é par')
else:
    print(f'O número que você digitou é {numero} e ele é impar')"""

"""
usuario = float(input("Que horas são?:  "))

if usuario <= 11:
    print("Bom dia")
elif usuario > 11 and usuario <= 17:
    print('Boa tarde')
else:
    print('Boa noite')"""

"""nome = str(input('Digite seu nome: '))
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')"""

"""contador = 0

while contador <10:
    contador += 1
    print(contador)"""


"""texto = 'Python' # Esse  codigo e o de baixo dele fazem exatamente a mesma coisa

i = 0
tam = len(texto)
while i < tam:
    print(texto[i])

    i += 1"""

"""texto = 'Python'

for letra in texto:
    print(letra)"""


# atividade de descobrir palavra secreta
"""secreta = 'Bahia'
p = ''
tentativas = 0
while True:
    palavra = str(input('Digite uma letra: '))
    tentativas += 1
    if len(palavra) > 1:
        print('Digite apenas uma letra')
        continue
    if palavra in secreta:
        p += palavra
    formada = ''
    for letra in secreta:
        if letra in p:
            formada += letra
        else:
            formada += '*'
    print('palavra formada', formada)
    if formada == secreta:
        print('VOCÊ GANHOU!! PARABÉNS!', secreta)
        print(f'Você tentou {tentativas}x até acertar')
        p = ''
        tentativas = 0"""

"""# Para criar um contador em uma lista
lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for i in indices:
    print(i, lista[i])"""
