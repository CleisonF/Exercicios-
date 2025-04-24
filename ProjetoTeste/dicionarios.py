pessoa = {
    'nome': 'Cleison',
    'sobrenome': 'Faleta',
    'idade': 28,
    'altura': 1.70,
    'endereço': [
        {'rua': 'tal','numero': 123},
        {'rua': 'outra rua', 'numero': 321}
    ],
}
#print(pessoa['endereço'])
for chave in pessoa:
    print(chave, pessoa[chave])