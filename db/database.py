from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# conexão com o banco mysql
engine = create_engine('mysql+pymysql://root:@localhost:3306/api.db')
conn = engine.connect()

Base = declarative_base()


# cria a classe base que representa a tabela de usuário, criando colunas id, email e senha
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    senha = Column(String(255), nullable=False)
