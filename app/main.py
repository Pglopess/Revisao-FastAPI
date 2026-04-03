from fastapi import FastAPI

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