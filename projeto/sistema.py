from time import sleep
from lib.arquivo import ver_cadastro, adicionar_aluno, remover_aluno_id, editar_aluno_id
from lib.interface import menu, cabecalho, leiaInt



while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Apagar cadastro','Editar aluno' ,'Sair do Sistema'])
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
        while True:
            turno = input('Turno (Matutino/Vespertino): ').capitalize()
            if turno in ['Matutino', 'Vespertino']:
                break
            print('Turno inválido. Digite Matutino ou Vespertino.')

        adicionar_aluno(nome, idade, posicao, numero_camisa, contato, turno)

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
        editar_aluno_id()

    elif resposta == 5:
        cabecalho('Saindo do sistema.... Até logo')
        break
    else:
        print('\033[0;31mErro! Digite uma opção valida!\033[m')
