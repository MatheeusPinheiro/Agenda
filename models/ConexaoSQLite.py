import sqlite3
from models.ConexaoDB import ConexaoDB

class ConexaoSQLite(ConexaoDB):
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = sqlite3.connect(self.nome_banco)
            self.cursor = self.conexao.cursor()
            print(f"Conexão com o banco de dados '{self.nome_banco}' estabelecida.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada.")

    def executar_comando(self, comando, parametros: None) -> None:
        try:

            if parametros:
                self.cursor.execute(comando, parametros)
            else:
                self.cursor.execute(comando)
            
            self.conexao.commit()
        
        except sqlite3.Error as ex:
            print(f'Erro ao executar comando SQLite: {ex}')

    def consultar(self, consulta, parametros = None) -> None:
        try:
            if parametros:
                self.cursor.execute(consulta, parametros)
            else:
                self.cursor.execute(consulta)
            
            return self.cursor.fetchall()
        
        except sqlite3.Error as ex:
            print(f'Erro ao consultar SQLite: {ex}')
            return None
        
    