from pydantic import BaseModel

class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int
    disponivel: bool = True

class Autor(BaseModel):
    nome: str
    nacionalidade: str
    ativo: bool = True