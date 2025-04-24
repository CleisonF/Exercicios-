#perguntas = [
#    {
#        'Pergunta': 'Quanto é 2+2',
#        'Opções': ['1', '3', '4', '5'],

#    },
#]
#print(perguntas)
#resp = int(input('Qual a sua resposta na questão acima: '))
#cont = 1
#while resp !=4:
#    cont += 1
#    if resp == 4:
#        print('Resposta correta!')
#        break
#    else:
#        print('Você errou! tente novamente')
#        resp = int(input('Qual a sua resposta na questão acima: '))
#print(f'você tentou {cont}x até acertar')


perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2 ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51' ],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()

    escolha = int(input('Escolha uma opção: '))
    acertou = False
    qtd_opcoes = len(opcoes)
    if escolha >=0 and escolha < qtd_opcoes:
        if opcoes[escolha] == pergunta['Resposta']:
            acertou = True

    if acertou:
        print('Acertou ')
        qtd_acertos +=1
    else:
        print('Não acertou')

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas')