from fastapi import FastAPI
from pydantic import BaseModel
import db

app = FastAPI()

class NomeIn(BaseModel):
    nome: str

@app.get("/")
def root():
    return{"status": "ok", "message":"API funcionando!"}

@app.get("/nomes")
def mostrar_nomes():
    nomes = db.mostrar_nomes()
    return {"nomes": nomes}

@app.post("/adicionar")
def inserir_nome(dados: NomeIn):
    nome = dados.nome.strip().capitalize()

    if nome == "":
        return {"ok": False, "error": "Nome inválido"}
    
    if db.inserir_nome(nome):
        return {"ok": True, "message": "Nome cadastrado com sucesso"}
    else:
        return{"ok": False, "error": "Nome já existe"}
    