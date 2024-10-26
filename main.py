from models.agenda import Agenda
from models.contato import Contato
import os


def menu():
    print('1. Adicionar contato')
    print('2. Atualizar contato')
    print('3. Listar contatos')
    print('4. Remover Contato')
    print('5. Sair do programa')
    return input('Informe sua opção: ')

def limpar_tela():
    if os.name == 'nt':
        os.system('CLS')


def pegar_dados():
    nome = input('Informe o nome do novo contato: ')
    telefone = input('Informe o telefone do novo contato: ')
    email = input('Informe o e-mail do novo contato: ')
    return nome, telefone, email


def espera():
    return input('Pressione qualquer tecla para continuar...')


def main():

    agenda = Agenda(r'D:\banco\agenda.db')

    while True:
        limpar_tela()
        opcao = menu()

        match opcao:

            case '1':
               limpar_tela()
               nome, telefone, email = pegar_dados()
               contato = Contato(nome, telefone, email)
               agenda.adicionar_contato(contato)
               espera()
            case '2':
                pass

            case '3':
                limpar_tela()
                contatos = agenda.listar_contatos()

                if len(contatos) > 0:
                    print('### Lista de Contatos ###')
                    for contato in contatos:
                        print(contato)
                        # print(f'Nome: {nome} Telefone: {telefone}, E-mail: {email}')
                
                else:
                    print('### Lista de Contatos ###')
                    print('Nenhum contato cadastrado.')

                espera()

            case '4':
                pass

            case '5':
                limpar_tela()
                print('Obrigado por usar o programa..')
                break
            case _:
                limpar_tela()
                print('Opção inválida, digite uma oção de (1 a 5)')
                





if __name__ == '__main__':
    main()