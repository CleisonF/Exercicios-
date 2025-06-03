from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo)
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro')
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('exception.txt','w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)