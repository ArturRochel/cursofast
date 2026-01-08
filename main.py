from fastapi import FastAPI

app = FastAPI(title="API Pizzaria", description="Está é a API que estou construindo para aprender sobre FastAPI e colocar os meus conhecimentos em prática", version="7.7.7")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)