from logging import exception

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError: #Para colocar mais de um except é preciso nomear todos eles.
            print('Não foi possivel apagar este indice')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido!')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
                print(i, valor)
    else:
        print('Por favor escolha i, a ou l.')