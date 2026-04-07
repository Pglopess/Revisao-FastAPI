from fastapi import FastAPI
from app.routers import dados, analises

app = FastAPI()

app.include_router(dados.router)
app.include_router(analises.router)

@app.get("/")
def root():
    return {"mensagem": "API funcionando!"}