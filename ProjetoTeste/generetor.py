"""def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Dando continuidade...')
    yield 3
    print('terminando')
    return 'Acabou'


gen = generator(n=0)
for n in gen:
    print(n)"""

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return



gen = generator()
for n in gen:
    print(n)