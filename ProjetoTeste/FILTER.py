def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]
new_product = [
    p for p in produtos
    if p['preco'] > 10
]

#no filtrer é usado assim
novo_p = filter(
    lambda p: p['preco'] >10, produtos
)

#tanto o new_product e o novo_p fazem a mesma coisa que é filtrar.


print_iter(produtos)
print_iter(new_product)
print_iter(novo_p)