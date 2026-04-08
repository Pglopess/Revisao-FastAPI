# Revisão FastAPI — Fase 3

API REST construída com FastAPI durante a revisão da Fase 3 do plano de estudos backend Python.

Conecta a um banco SQLite, processa dados com Pandas e valida entradas com Pydantic.

---

## Endpoints

### Geral

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Verifica se a API está no ar |

### Livros

| Método | Rota | Parâmetros | Descrição |
|--------|------|------------|-----------|
| GET | `/livros` | `autor` (query, opcional) | Lista todos os livros, com filtro opcional por autor |
| GET | `/livros/{livro_id}` | `livro_id` (path, obrigatório) | Busca um livro pelo ID |
| POST | `/livros` | body JSON | Cria um livro novo |

**Exemplo de body para POST /livros:**
```json
{
  "titulo": "Clean Code",
  "autor": "Robert Martin",
  "ano": 2008,
  "disponivel": true
}
```

### Análises

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/analises/resumo` | Resumo geral do acervo com agregações por autor |
| GET | `/analises/disponibilidade` | Porcentagem de livros disponíveis |

---

## Como instalar e rodar

**Pré-requisitos:** Python 3.10+

**1. Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/Revisao-FastAPI.git
cd Revisao-FastAPI
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Popule o banco de dados**
```bash
python scripts/populate_db.py
```

**5. Rode a API**
```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`

---

## Documentação automática

Com a API rodando, acesse:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Estrutura do projeto

```
Revisao FastAPI/
├── app/
│   ├── main.py          # instância do FastAPI e inclusão dos routers
│   ├── database.py      # conexão com SQLite
│   ├── models.py        # modelos Pydantic
│   └── routers/
│       ├── dados.py     # rotas de livros
│       └── analises.py  # rotas de análise com Pandas
├── scripts/
│   └── populate_db.py   # popula o banco com dados iniciais
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```