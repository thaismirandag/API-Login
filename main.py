from fastapi import FastAPI 
from db import database
from db.database import User, engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException


app = FastAPI()


@app.get("/")
def root():
    return "Hello World!"


# gera toda a estrutura do banco
database.Base.metadata.create_all(engine)


# Cria a classe Usuario
class Usuario(BaseModel):
    email: str
    senha: str


@app.post("/users")
def cria_usuario(user: Usuario):
    # inicializa a sessão
    session = Session(bind=engine, expire_on_commit=False)
    # cria instancia class User
    usuariodb = User(email=user.email, senha=user.senha)
    session.add(usuariodb)
    session.commit()
    session.close()

    return f"Usuario de id {usuariodb.id} foi cadastrado com sucesso!"


@app.get("/users/{email}")
def login(email: str, senha: str):
    session = Session(bind=engine, expire_on_commit=False)
    user = session.query(User).filter(User.email == email, User.senha == senha).first()
    session.close()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return user


@app.delete("/users")
def deleta_usuario(email: str, senha: str):
    session = Session(bind=engine, expire_on_commit=False)
    user = session.query(User).filter(User.email == email).first()

    if user:
        session.delete(user)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    return "Deletado"


@app.put("/users")
def atualiza_usuario(email: str, senha: str):
    session = Session(bind=engine, expire_on_commit=False)
    user = session.query(User).filter(User.email == email).first()

    if user:
        user.senha = senha
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    return user









