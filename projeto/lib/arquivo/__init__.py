from conexao import conectar
import mysql.connector


#função para mostrar os dados que estão dentro do arquivo
def ver_cadastro():
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        print('\nDeseja listar alunos de qual turno?')
        print('[1] Matutino')
        print('[2] Vespertino')
        print('[3] Todos')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            cursor.execute("SELECT * FROM alunos WHERE turno = %s ORDER BY nome", ('Matutino',))
        elif opcao == '2':
            cursor.execute("SELECT * FROM alunos WHERE turno = %s ORDER BY nome", ('Vespertino',))
        elif opcao == '3':
            cursor.execute("SELECT * FROM alunos ORDER BY nome")
        else:
            print('\nOpção inválida.')
            return

        dados = cursor.fetchall()

        if not dados:
            print('\nNenhum aluno cadastrado no momento.\n')
        else:
            print("\n--- Alunos Cadastrados ---")
            for aluno in dados:
                print(f'ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Posição: {aluno[3]} | Camisa: {aluno[4]} | Contato: {aluno[5]} | Turno: {aluno[6]}')

        conn.commit()

    except mysql.connector.Error as err:
        print(f'Erro ao listar alunos: {err}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# função de cadastrar novo item no banco de dados
def adicionar_aluno(nome, idade, posicao, numero_camisa, contato, turno):
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "INSERT INTO alunos (nome, idade, posicao, numero_camisa, contato, turno) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nome, idade, posicao, numero_camisa, contato, turno)

        cursor.execute(sql, valores)
        conn.commit()
        print(f'\nAluno {nome} cadastrado com sucesso!')
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar aluno: {err}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



#função de apagar um aluno por id.
def remover_aluno_id(id_aluno):
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM alunos WHERE id = %s', (id_aluno,))
        aluno = cursor.fetchone()

        if aluno:
            print(f"\nAluno encontrado: {aluno}")
            confirmar = input(f"Tem certeza que deseja remover o aluno com ID {id_aluno}? (s/n): ").strip().lower()

            if confirmar == 's':
                cursor.execute('DELETE FROM alunos WHERE id = %s', (id_aluno,))
                conn.commit()
                print(f'\nAluno com ID {id_aluno} removido com sucesso.')
            else:
                print('\nRemoção cancelada.')
        else:
            print(f'\nNenhum aluno encontrado com ID {id_aluno}.')

    except mysql.connector.Error as err:
        print(f"Erro ao remover aluno: {err}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


## Função para editar um aluno já cadastrado
def editar_aluno_id():
    conn = conectar()
    cursor = conn.cursor()

    id_aluno = input('Digite o ID do aluno que deseja editar: ')
    cursor.execute('SELECT * FROM alunos WHERE id = %s', (id_aluno,))
    aluno = cursor.fetchone()

    if aluno:
        print(f"\nAluno atual: {aluno}")
        nome = input('Novo nome (pressione Enter para manter): ') or aluno[1]
        idade = input('Nova idade (pressione Enter para manter): ') or aluno[2]
        posicao = input('Nova posição: ') or aluno[3]
        numero_camisa = input('Novo número da camisa: ') or aluno[4]
        contato = input('Novo número de contato: ') or aluno[5]
        turno = input('Novo turno: ') or aluno[6]

        cursor.execute('''
            UPDATE alunos
            SET nome = %s, idade = %s, posicao = %s, numero_camisa = %s, contato = %s, turno = %s
            WHERE id = %s
        ''', (nome, idade, posicao, numero_camisa, contato,turno, id_aluno))
        conn.commit()
        print("\nCadastro atualizado com sucesso.")
    else:
        print(f"\nNenhum aluno encontrado com ID {id_aluno}.")

    cursor.close()
    conn.close()