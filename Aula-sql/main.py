import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: Fazendo delete sem where
cursor.execute(f'DELETE FROM {TABLE_NAME}')

#DELETE mais cuidadoso
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
#CUIDADO: sql injection
sql = (f'INSERT INTO {TABLE_NAME} (name, weight)'
                'VALUES (:nome, :peso)')
cursor.execute(sql, {'nome': 'Pelé', 'peso': 6})
cursor.executemany(sql, ({'nome': 'Joana','peso': 4},
                         {'nome': 'Luiz','peso': 5}))
connection.commit()


if __name__ == '__main__':
    print(sql)
    cursor.close()
    connection.close()
