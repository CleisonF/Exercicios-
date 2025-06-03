import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / 'aula_pathlib.csv'#para criar um caminho completo do arquivo


lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]
with open(caminho_csv, 'w') as arquivo:#para criar um arquivo csv
    nome_colunas = lista_clientes[0].keys()#variavel para coletar apenas o primeiro objeto de cada lista ex: Nome
    escritor = csv.writer(arquivo)#para escrever no arquivo

    escritor.writerow(nome_colunas)#para adicionar a lista de clientes no arquivo pela variavel nome_colunas
    for cliente in lista_clientes:#para escrever todos os valores da lista completa uma por uma
       print(cliente.values())
       escritor.writerow(cliente.values())

#with open(caminho_csv, 'r') as arquivo:
    #leitor = csv.reader(arquivo)

    #print(next(leitor))

#with open(caminho_csv, 'r') as arquivo: #para ler o arquivo em forma de dicionario
    #leitor = csv.DictReader(arquivo)

    #print(next(leitor))