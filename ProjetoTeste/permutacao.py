from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz','Leticia',
]
camiseta = [
    ['preta', 'branca'],
    ['pp','p', 'm', 'g', 'gg'],
    ['masculino', 'femenino']
]

print_iter(product(*camiseta))
print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))