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

    agenda = Agenda(r'D:\bancos\agenda.db')

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

                limpar_tela()
                nome_contato = input('Informe o nome do contato que deseja atualizar: ')
                dados = agenda.buscar_contato(nome_contato)

                if dados:
                    #dados antigos
                    id_contato, nome_antigo, telefone_antigo, email_antigo = dados[0]
                
                    limpar_tela()

                    nome, telefone, email = pegar_dados()

                    if len(nome) == 0: nome = nome_antigo
                    if len(telefone) == 0: telefone = telefone_antigo
                    if len(email) == 0: email = email_antigo

                    contato_atualizado = Contato(nome, telefone, email)
                    contato_atualizado._Contato__id = id_contato
                    agenda.atualizar_contato(contato_atualizado)

                    print('Contato atualizado com sucesso.')
                    espera()
                
                else:
                    limpar_tela()
                    print('Contato não encontrado.')
                    espera()

            case '3':
                limpar_tela()
                contatos = agenda.listar_contatos()

                if len(contatos) > 0:
                    print('### Lista de Contatos ###')
                    for contato in contatos:
                        nome, telefone, email = contato
                        print(f'Nome: {nome} Telefone: {telefone}, E-mail: {email}')
                
                else:
                    print('### Lista de Contatos ###')
                    print('Nenhum contato cadastrado.')

                espera()

            case '4':
                limpar_tela()
                nome_contato = input('Informe o nome do contato que deseja excluir: ')
                dados = agenda.buscar_contato(nome_contato)

                if dados:
                    #dados antigos
                    id_contato = dados[0][0]
                  
                    agenda.remover_contato(id_contato)
                    espera()
                
                else:
                    limpar_tela()
                    print('Contato não encontrado.')
                    espera()

            case '5':
                limpar_tela()
                print('Obrigado por usar o programa..')
                break
            case _:
                limpar_tela()
                print('Opção inválida, digite uma oção de (1 a 5)')
                espera()
    
    





if __name__ == '__main__':
    main()