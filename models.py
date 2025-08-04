from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

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
# ItensPedido



# executa a criação dos metadados do seu banco de dados

