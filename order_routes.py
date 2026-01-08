from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@order_router.get("/", description="Rota para listagem de pedidos", name="Listagem de pedidos")
async def listar_pedidos():
    return {"lista_pedidos": [{"pedido": "batata frita"}, {"pedido": "Coca Cola Zero, cachorro quente, pizza"}]}