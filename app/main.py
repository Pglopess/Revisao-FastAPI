from fastapi import FastAPI, HTTPException
from app.models import Autor, Livro
from app.database import get_connection
import pandas as pd

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

@app.get("/analises/resumo")
def resumo_livros():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM livros", conn)
    conn.close()

    resumo = {
        "total_livros": int(df.shape[0]),
        "disponiveis": int(df["disponivel"].sum()),
        "indisponiveis": int((df["disponivel"] == 0).sum()),
        "livros_por_autor": df.groupby("autor")["titulo"].count().to_dict(),
        "ano_mais_antigo": int(df["ano"].min()),
        "ano_mais_recente": int(df["ano"].max()),
    }

    return resumo