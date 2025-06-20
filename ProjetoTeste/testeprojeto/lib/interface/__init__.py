def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro: por favor, digite um número inteiro válido. \033[m')
        except (KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompido pelo usuario.\033[m')
            return 0
        else:
            return n



def linha(tam = 60):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(60))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
