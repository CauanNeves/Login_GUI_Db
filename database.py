import sqlite3
import os

# Verificando se o diretório existe, caso não exista, cria
os.makedirs('C:\\db_users', exist_ok=True)

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.create_table()  # Criando a tabela no momento da inicialização

    def create_table(self):
        #Cria a tabela 'users' se não existir.
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                );
            ''')
            conn.commit()

    def add(self, user, hash):
        #Adiciona um novo usuário ao banco de dados.
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (user, hash))
                conn.commit()
                return True  # Retorna True se o cadastro for bem-sucedido
            except sqlite3.IntegrityError:
                return False  # Retorna False se o usuário já existir

    def get_user(self, username):
        #Busca o usuário no banco de dados e retorna a hash da senha, se encontrado.
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
            return cursor.fetchone()  # Retorna (password_hash,) ou None
    
    def table_exists(self):
        #Verifica se a tabela 'users' existe no banco de dados
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="users";')
            return cursor.fetchone() is not None  # Retorna True se a tabela existir, False caso contrário