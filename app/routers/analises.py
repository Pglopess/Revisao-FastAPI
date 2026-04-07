import pandas as pd
from fastapi import APIRouter
from app.database import get_connection

router = APIRouter()

@router.get("/analises/resumo")
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