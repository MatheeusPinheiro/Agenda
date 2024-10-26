from abc import ABC, abstractmethod


class ConexaoDB(ABC):

    @abstractmethod
    def conectar(self) -> None: pass

    @abstractmethod
    def fechar_conexao(self) -> None: pass

    @abstractmethod
    def executar_comando(self, comando: str, parametros = None) -> None: pass

    @abstractmethod
    def consultar(self, consultar, parametros = None) -> None: pass