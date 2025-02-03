import sqlite3
import os

#Verificando se o diretório existe, caso não exista crio um

os.makedirs('C:\\db_users', exist_ok= True)

class Database:
    def __init__(self, db_path):
        self.db_path= db_path
    
    def add(self, user, hash):
        #Conectando ao Banco de Dados
        with sqlite3.connect(self.db_path) as conn:
            cursor= conn.cursor()
            #criando a tabela
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           user TEXT NOT NULL,
                           hash TEXT NOT NULL
            );
            ''')
            #Adicionando dados
            cursor.execute('INSERT INTO users (user, hash) VALUES (?, ?)', (user, hash))

if __name__ == '__main__':
    db = Database
    db.add('Cauan', 'deba0172511d5701d964202f4e5de698d5e07c67')