from time import sleep
from testeprojeto.lib.arquivo import ver_cadastro, adicionar_aluno, remover_aluno_id
from testeprojeto.lib.interface import menu, cabecalho, leiaInt



while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Apagar cadastro', 'Sair do Sistema'])
    sleep(1)
    if resposta == 1:
        ver_cadastro()
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        posicao = str(input('Sua posição: '))
        numero_camisa = leiaInt('Numero da camisa: ')
        contato = leiaInt('Numero de contato: ')
        adicionar_aluno(nome, idade, posicao, numero_camisa, contato)

    elif resposta == 3:
        while True:
            id_input = input('Qual ID do aluno você quer apagar? ')
            try:
                id_aluno = int(id_input)
                break
            except ValueError:
                print('\033[0;31mErro: O ID deve ser um número inteiro válido.\033[m')
        remover_aluno_id(id_aluno)
    elif resposta == 4:
        cabecalho('Saindo do sistema.... Até logo')
        break
    else:
        print('\033[0;31mErro! Digite uma opção valida!\033[m')
