from time import sleep
from testeprojeto.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

#função para mostrar os dados que estão dentro do arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt') # abre e ler o arquivo
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:<3}anos  Posição:{dado[2]:>3}')
            print(f'Camisa:{dado[3]:<22} Numero de contato:{dado[4]} ')
            sleep(1)
    finally:
        a.close()

# função de cadastrar novo item no arquivo
def cadastrar(arq, nome='desconhecido', idade=0, posi = 'Sem posição', camisa=0, numctt=0):
    try:
        a = open(arq,'at') # abre o arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade};{posi};{camisa};{numctt}\n')
        except:
            print('Houve um Erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


#função de apagar e organizar o arquivo
def apagarRegistro(arq, valor):
    try:
        with open(arq, 'rt') as file:
            linhas = file.readlines()

        novas_linhas = [linha for linha in linhas if valor not in linha]

        # Cria uma nova lista, excluindo as linhas que contêm o valor a ser removido
        if len(novas_linhas) < len(linhas):
            with open(arq, 'wt') as file:
                file.writelines(novas_linhas)
            print(f'O "{valor}" removido com sucesso!')
        else:
            print(f'Registro "{valor}" removido com sucesso!')

    except FileNotFoundError:
        print(f'Erro: O arquivo {arq} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')