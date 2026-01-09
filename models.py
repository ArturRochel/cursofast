from sqlalchemy import create_engine, Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

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

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) 
    cliente = Column("cliente", ForeignKey("usuarios.id"))
    preco = Column("preco", Numeric(10,2))

    def __init__(self, status, cliente, preco):
        self.status = status
        self.cliente = cliente
        self.preco = preco

class ItemPedido(Base):

    # TAMANHO_PIZZAS = (
    #     ("PEQUENA", "PEQUENA"),
    #     ("MEDIA", "MEDIA"),
    #     ("GRANDE", "GRANDE"),
    #     ("GIGANTE", "GIGANTE")
    # )

    # SABORES_PIZZAS = (
    #     ("CALABRESA", "CALABRESA"),
    #     ("MARGUERITA", "MARGUERITA"),
    #     ("FRANGO", "FRANGO"),
    #     ("FRANGO COM CATTUPIRY", "FRANGO COM CATTUPIRY")
    # )

    __tablename__ = "itens"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    nome = Column("nome", String, nullable=False)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco", Numeric(10, 2), nullable=False)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, nome, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.nome = nome
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido