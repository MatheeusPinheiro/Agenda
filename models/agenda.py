from models.contato import Contato
from models.ConexaoSQLite import ConexaoSQLite


class Agenda:

    def __init__(self, nome_banco: str) -> None:
        self.__conexao = ConexaoSQLite(nome_banco)
        self.__conexao.conectar()

    def adicionar_contato(self, contato: Contato) -> None:
        comando = "INSERT INTO tb_contatos (NOME_CONTATO, TELEFONE_CONTATO, EMAIL_CONTATO) VALUES (?, ?, ?)"
        self.__conexao.cursor.execute(comando, (contato.nome, contato.telefone, contato.email))
        self.__conexao.conexao.commit()
        print(f'Contato {contato.nome} adicionado com sucesso.')

    def listar_contatos(self) -> None:
        comando = "SELECT NOME_CONTATO, TELEFONE_CONTATO, EMAIL_CONTATO FROM tb_contatos"
        self.__conexao.cursor.execute(comando)
        resultados = self.__conexao.cursor.fetchall()
        return resultados

    def atualizar_contato(self, contato: Contato) -> None:
        comando = "UPDATE tb_contatos SET  NOME_CONTATO = ?, TELEFONE_CONTATO = ? , EMAIL_CONTATO = ? WHERE ID_CONTATO = ? "
        self.__conexao.cursor.execute(comando, (contato.nome, contato.telefone, contato.email, contato.id))
        self.__conexao.conexao.commit()

    def remover_contato(self, contato_id) -> None:
        comando = "DELETE FROM tb_contatos WHERE ID_CONTATO = ?"
        self.__conexao.cursor.execute(comando, (contato_id,))
        self.__conexao.conexao.commit()
        print(f'Contato de ID {contato_id}, removido com sucesso.')
