from sqlalchemy import create_engine, Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base

database = create_engine(url="sqlite:///banco.db")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)

    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String, default="pendente") #pendente, cancelado, finalizado
    cliente = Column("cliente", ForeignKey("usuarios.id"))
    itens = Column("itens")
    preco = Column("preco", Float)

    def __init__(self, status="pendente", cliente, itens, preco):
        self.cliente = cliente
        self.status = status
        self.itens = itens
        self.preco = preco

class ItemPedido(Base):
    __tablename__ = "itens"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    nome = Column("nome", String, nullable=False)
    preco = Column("preco", Numeric(10, 2), nullable=False)

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco