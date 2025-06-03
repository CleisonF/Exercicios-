import json
import os

nome_arquivo ='aula_json.json'
#cria um caminho completo do inicio até o fim
caminho_absoluto = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        nome_arquivo
    )
)
#print(os.path.dirname(__file__), nome_arquivo)
filme = {'title': 'O senhor dos anéis: A Sociedade do Anel',
         'original_title': 'The Lord od the Rings: The fellowship of the Ring',
         'is_movie': True,
         'imdb_rating': 8.8,
         'year': 2001,
         'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
         'buget': None}
with open(caminho_absoluto, 'w') as arquivo: #feito para enviar e escrever um arquivo e salvar em uma pasta
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)#ensure serve para que o sistema leia os acentos e "Ç" entre outros

with open(caminho_absoluto, 'r') as arquivo: #feito para ler o arquivo
    filme_do_json = json.load(arquivo)
    print(filme_do_json)