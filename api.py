from fastapi import FastAPI
from pydantic import BaseModel
import db

app = FastAPI()

class NomeIn(BaseModel):
    nome: str

class NomeUpdateIn(BaseModel):
    nome_antigo: str
    nome_novo: str

@app.get("/")
def root():
    return{"status": "ok", "message":"API funcionando!"}

@app.get("/nomes")
def mostrar_nomes():
    nomes = db.mostrar_nomes()
    return {"nomes": nomes}

@app.post("/nomes")
def inserir_nome(dados: NomeIn):
    nome = dados.nome.strip().capitalize()

    if nome == "":
        return {"ok": False, "error": "Nome inválido"}
    
    if db.inserir_nome(nome):
        return {"ok": True, "message": "Nome cadastrado com sucesso"}
    else:
        return{"ok": False, "error": "Nome já existe"}
    
@app.delete("/nomes/{nome}")
def deletar_nome(nome: str):
    nome = nome.strip().capitalize()

    if nome == "":
        return {"ok": False, "error": "Nome inválido"}
    
    if db.deletar_nome(nome):
        return {"ok": True, "message": "Nome deletado com sucesso"}
    else:
        return{"ok": False, "error": "Nome não consta nos registros"}
    
@app.put("/nomes")
def alterar_nome(dados: NomeUpdateIn):
    nome_antigo = dados.nome_antigo.strip().capitalize()
    nome_novo = dados.nome_novo.strip().capitalize()

    if nome_antigo == "" or nome_novo == "":
        return {"ok": False, "error": "Nome inválido"}
    elif nome_antigo == nome_novo:
        return {"ok": False, "error": "Os nomes são iguais, nada foi alterado"}
    
    validador = db.alterar_nome(nome_antigo, nome_novo)

    if validador == 0:
        return {"ok": False, "error":"O novo nome já consta em nossos registros"}
    elif validador:
        return {"ok": True, "message": "O nome foi alterado com sucesso"}
    else: 
        return {"ok": False, "error": "O nome a ser alterado não consta em nossos registros"}
    