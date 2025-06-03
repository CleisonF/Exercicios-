from functools import reduce
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]
#função que faz acumular "somar" o preço de varios produtos gerando um resultado total
def funcao_reduce(acumulador, produto):
    print('Acumulador', acumulador)
    print('Produto', produto)
    print()
    return acumulador + produto['preco']
#importante sempre passar um valor inicial no total para evitar erros.
total = reduce(funcao_reduce, produtos, 0)

print(f'total é {total}')

