# Pizzaria API 🍕 (FastAPI)

API de pedidos de uma pizzaria, desenvolvida como projeto de curso para iniciar os estudos em **FastAPI**, autenticação com JWT e integração com banco de dados usando SQLAlchemy. [web:6]

## Tecnologias utilizadas

- Python 3.11+
- FastAPI (`fastapi`, `starlette`) [web:6]
- SQLAlchemy 2.x para ORM [web:6]
- Alembic para migrações de banco de dados [web:3][web:11]
- SQLAlchemy-Utils para tipos e helpers adicionais (ex.: UUIDType, EmailType) [web:9]
- Pydantic v2 para validação de dados [web:6]
- Uvicorn como servidor ASGI [web:6]
- Autenticação com JWT (`python-jose`, `passlib`, `bcrypt`) [web:6]
- Carregamento de variáveis de ambiente com `python-dotenv` [web:10]
- Suporte a formulários/multipart (upload de arquivos, formulários HTML) com `python-multipart` [web:7][web:13]

## Funcionalidades previstas

- Cadastro e autenticação de usuários (login com JWT).
- CRUD de pizzas e/ou itens do cardápio.
- Criação, listagem, atualização e cancelamento de pedidos.
- Controle de status do pedido (por exemplo: aberto, em preparo, entregue).
- Separação de rotas de autenticação e pedidos (ex.: `auth_routes.py`, `order_routes.py`). [web:6]

## Como rodar o projeto localmente

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/seu-usuario/pizzaria-api.git
   cd pizzaria-api

# Alembic - Versionamento banco de dados

alembic init alembic

alembic revision --autogenerate -m "mensagem_de_migracao"

alembic upgrade head