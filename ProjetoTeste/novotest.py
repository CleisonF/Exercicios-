def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mult = multiplicar(1,2,3,4,5)
print(mult)

def parouimpar():
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        print(f'{num} é par')
        return num
    else:
        print(f'{num} é impar')

parouimpar()