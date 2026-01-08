# Pizzaria API 🍕 (FastAPI)

API de pedidos de uma pizzaria, desenvolvida como projeto de curso para iniciar os estudos em **FastAPI**, autenticação com JWT e integração com banco de dados usando SQLAlchemy. [web:18][web:26]

## Tecnologias utilizadas

- Python 3.11+
- FastAPI (`fastapi`, `starlette`) [web:26]
- SQLAlchemy 2.x para ORM [web:26]
- Pydantic v2 para validação de dados [web:26]
- Uvicorn como servidor ASGI [web:26]
- Autenticação com JWT (`python-jose`, `passlib`, `bcrypt`) [web:18][web:26]
- Carregamento de variáveis de ambiente com `python-dotenv` [web:24]

## Funcionalidades previstas

- Cadastro e autenticação de usuários (login com JWT).
- CRUD de pizzas e/ou itens do cardápio.
- Criação, listagem, atualização e cancelamento de pedidos.
- Controle de status do pedido (por exemplo: aberto, em preparo, entregue).
- Separação de rotas de autenticação e pedidos (ex.: `auth_routes.py`, `order_routes.py`). [web:18][web:20]

## Como rodar o projeto localmente

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/seu-usuario/pizzaria-api.git
   cd pizzaria-api
