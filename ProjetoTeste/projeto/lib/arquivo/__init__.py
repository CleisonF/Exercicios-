from testeprojeto.conexao import conectar
import mysql.connector


#função para mostrar os dados que estão dentro do arquivo
def ver_cadastro():
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alunos")
        dados = cursor.fetchall()

        if not dados:
            print('\nNenhum aluno cadastrado no momento.\n')
        else:
            print("\n--- Alunos Cadastrados ---")
            for aluno in dados:
                print(f'ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Posição: {aluno[3]} | Camisa: {aluno[4]} | Contato: {aluno[5]}')
            conn.commit()

    except mysql.connector.Error as err:
        print(f'Erro ao listar alunos: {err}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# função de cadastrar novo item no banco de dados
def adicionar_aluno(nome, idade, posicao, numero_camisa, contato):
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "INSERT INTO alunos (nome, idade, posicao, numero_camisa, contato) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, idade, posicao, numero_camisa, contato)

        cursor.execute(sql, valores)
        conn.commit()
        print(f'\nAluno {nome} cadastrado com sucesso!')
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar aluno: {err}")
        if conn: # Garante que, se a conexão estiver aberta, o rollback é feito
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
            cursor.execute('DELETE FROM alunos WHERE id = %s', (id_aluno,))
            conn.commit()
            print(f'\nAluno com ID {id_aluno} removido com sucesso.')
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