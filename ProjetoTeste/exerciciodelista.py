"""def zipper (lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo)]"""




li = ['Salvador','Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP','MG', 'RJ']
print(list(zip(li, l2)))