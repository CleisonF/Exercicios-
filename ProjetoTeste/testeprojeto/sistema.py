from testeprojeto.lib.arquivo import *
from testeprojeto.lib.interface import *


arq = 'testeprojeto.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Apagar cadastro', 'Sair do Sistema'])
    sleep(1)
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        posi = str(input('Sua posição: '))
        camisa = leiaInt('Numero da camisa: ')
        numctt = leiaInt('Numero de contato: ')
        cadastrar(arq, nome, idade, posi, camisa, numctt)
    elif resposta == 3:
        apagar = str(input('Qual você quer apagar? '))
        apagarRegistro(arq, apagar)
        continue
    elif resposta == 4:
        cabecalho('Saindo do sistema.... Até logo')
        break
    else:
        print('\033[0;31mErro! Digite uma opção valida!\033[m')
