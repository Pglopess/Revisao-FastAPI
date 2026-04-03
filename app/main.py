from fastapi import FastAPI
from app.models import Autor, Livro  # adiciona no topo, junto com os outros imports

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "API funcionando!"}

@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int):
    return {"livro_id": livro_id, "titulo": "Livro de exemplo"}

@app.get("/livros")
def listar_livros(autor: str = None, pagina: int = 1):
    return {"autor": autor, "pagina": pagina}

@app.post("/livros", status_code=201)
def criar_livro(livro: Livro):
    return {"mensagem": "Livro criado com sucesso", "livro": livro}

@app.post("/autores", status_code=201)
def criar_autor(autor: Autor):
    return {"mensagem": "Autor criado com sucesso", "autor": autor}