from fastapi import FastAPI, HTTPException
from app.models import Autor, Livro
from app.database import get_connection

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "API funcionando!"}

@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
    livro = cursor.fetchone()
    conn.close()

    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    return dict(livro)

@app.get("/livros")
def listar_livros(autor: str = None):
    conn = get_connection()
    cursor = conn.cursor()

    if autor:
        cursor.execute("SELECT * FROM livros WHERE autor = ?", (autor,))
    else:
        cursor.execute("SELECT * FROM livros")

    livros = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return livros

@app.post("/livros", status_code=201)
def criar_livro(livro: Livro):
    return {"mensagem": "Livro criado com sucesso", "livro": livro}

@app.post("/autores", status_code=201)
def criar_autor(autor: Autor):
    return {"mensagem": "Autor criado com sucesso", "autor": autor}