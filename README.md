# Sistema de Biblioteca

Sistema simples de gerenciamento de livros feito em Django.

## Funcionalidades
- Cadastrar livros
- Editar livros
- Excluir livros
- Buscar por título ou autor

## Como rodar o projeto

1. Clone o repositório
   git clone https://github.com/julioprattes-stack/Projeto-Sistema-de-Biblioteca.git

2. Crie e ative um ambiente virtual
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Linux/Mac

3. Instale as dependências
   pip install -r requirements.txt

4. Rode as migrations
   python manage.py migrate

5. Inicie o servidor
   python manage.py runserver

## Tecnologias
- Python
- Django
- SQLite