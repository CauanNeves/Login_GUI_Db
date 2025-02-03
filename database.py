import sqlite3
import os

#Verificando se o diretório existe, caso não exista crio um

os.makedirs('C:\\database', exist_ok= True)

class Database:
    def __init__(self, db_path):
        self.db_path= db_path
    
    def add(self, user, hash):
        #Conectando ao Banco de Dados
        with sqlite3.connect(self.db_path) as conn:
            cursor= conn.cursor()

            #criando a tabela
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS 
            ''')