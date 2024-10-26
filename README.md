# Agenda de Contatos 📔

Este projeto é uma aplicação de agenda de contatos construída em Python. Utiliza uma estrutura de classes para organizar contatos e gerenciar a conexão com um banco de dados, permitindo a fácil adaptação para diferentes bancos SQL (como SQLite, PostgreSQL, entre outros).

## Tabela de Conteúdos

- [Descrição do Projeto](#descrição-do-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Exemplos de Código](#exemplos-de-código)
- [Licença](#licença)

## Descrição do Projeto

A aplicação de Agenda de Contatos permite adicionar, listar, atualizar e remover contatos de um banco de dados SQL. Com uma estrutura flexível e extensível, a aplicação suporta múltiplas implementações de bancos de dados e permite fácil adaptação para outras soluções SQL.

## Estrutura do Projeto

O projeto é composto por três classes principais:

1. **ConexaoDB**: Interface que define os métodos necessários para gerenciar a conexão com o banco de dados.
2. **ConexaoSQLite** e **ConexaoPostgreSQL**: Implementações específicas da interface para SQLite e PostgreSQL, respectivamente.
3. **Agenda**: Gerencia os contatos armazenados no banco de dados.
4. **Contato**: Representa um contato individual, com atributos como `nome`, `telefone` e `email`.

## Pré-requisitos

- **Python 3.8+**
- **Bibliotecas necessárias**:
  - Para SQLite: Biblioteca padrão do Python (`sqlite3`)
  - Para PostgreSQL: `psycopg2` (se estiver utilizando PostgreSQL)

Para instalar `psycopg2`, você pode usar o comando:
```bash
pip install psycopg2
