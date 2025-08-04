from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

# criar a conexão do banco de dados
db = create_engine("sqlite:///banco.db")


# cria a base do banco de dados
Base = declarative_base()

# criar as classes/tables 
# Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, unique=True, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


# Pedido

class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("FINALIZADO", "FINALIZADO"),
    #     ("CANCELADO", "CANCELADO")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"), nullable=False)
    preco = Column("preco", Float, nullable=False)

    def __init__(self, usuario, status = "PENDENTE", preco = 0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
# ItensPedido

class itemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String, nullable=False)
    tamanho = Column("tamanho", String, nullable=False)
    preco_unitario = Column("preco_unitario", Float, nullable=False)
    pedido = Column("pedido", ForeignKey("pedidos.id"), nullable=False)

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido



# executa a criação dos metadados do seu banco de dados

