from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from app.models import Autor, Livro  # adiciona no topo, junto com os outros imports

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "API funcionando!"}

livros_db = {
    1: {"titulo": "Clean Code", "autor": "Robert Martin"},
    2: {"titulo": "O Cortiço", "autor": "Aluísio Azevedo"},
}

@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int):
    if livro_id not in livros_db:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livros_db[livro_id]

@app.get("/livros")
def listar_livros(autor: str = None, pagina: int = 1):
    return {"autor": autor, "pagina": pagina}

@app.post("/livros", status_code=201)
def criar_livro(livro: Livro):
    return {"mensagem": "Livro criado com sucesso", "livro": livro}

@app.post("/autores", status_code=201)
def criar_autor(autor: Autor):
    return {"mensagem": "Autor criado com sucesso", "autor": autor}