import locale
from datetime import datetime
import string
from pathlib import Path

Caminho_arquivo = Path(__file__).parent / 'aula_template.txt'

locale.setlocale(locale.LC_ALL,'')

def converte_para_brl(numero: float) -> str:
    brl = 'R$' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2022,12,28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone= '+55 (71) 9 8349-4948'
)
with open(Caminho_arquivo, 'r') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
