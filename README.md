# FastAPI-mvc

Esse projeto possui o intuito de cadastrar usuários. O projeto segue o padrão de arquitetura Model-View-Controller (MVC). 

A camada view ainda não foi construída. Dessa forma, para que os endpoints pudessem ser testados, alterei a annotation para routers, assim pode ser testado no Postman.

# Tecnologias
- **FastAPI:**  Uma estrutura web moderna, rápida (de alto desempenho) para construção de APIs com Python 3.7+.
- **Uvicorn:** Um servidor ASGI extremamente rápido, usado para executar aplicativos FastAPI.
- **PyMySQL:** A pure-Python MySQL client library.
- **SQLAlchemy:** um kit de ferramentas SQL e uma biblioteca de mapeamento relacional de objetos (ORM) para Python.
- **Alembic:** Uma ferramenta de migração de banco de dados para SQLAlchemy.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/cafecomdeploy/hub-user-management.git
    ```
2. Instale as dependências:

    ```bash
    pip install -r .\requirements.txt
    ```
