from fastapi import APIRouter

auth_router = APIRouter(prefix="/autenticacao", tags=["Autenticação"])


@auth_router.get("/", name="Autenticação", description="Rota para executar o processo de autenticação da API.")
async def autenticar():
    return {"mensagem": "Usuário autenticado com sucesso"}