
class Contato:
    
    def __init__(self, nome: str, telefone: str, email: str) -> None:
        self.__id = None
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    @property
    def id(self):
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome) -> None:
        if not isinstance(nome, str) and len(nome.strip()) == 0:
            raise ValueError('Por favor, informe um nome válido.')
        self.__nome =  nome

    @property
    def telefone(self) -> str:
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone) ->  None:
        if not isinstance(telefone, str) and len(telefone.strip()) == 0:
            raise ValueError('Por favor, informe um telefone válido.')
        self.__telefone = telefone

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email) ->  None:
        if not isinstance(email, str) and len(email.strip()) == 0:
            raise ValueError('Por favor, informe um email válido.')
        self.__email = email

    def __str__(self):
        return f'Nome: {self.__nome}, Telefone: {self.__telefone}, E-mail: {self.__email}'

