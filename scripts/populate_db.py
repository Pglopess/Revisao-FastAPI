import sqlite3

DB_PATH = "biblioteca.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        disponivel INTEGER DEFAULT 1
    )
""")

cursor.executemany("""
    INSERT INTO livros (titulo, autor, ano, disponivel)
    VALUES (?, ?, ?, ?)
""", [
    ("Clean Code", "Robert Martin", 2008, 1),
    ("O Cortiço", "Aluísio Azevedo", 1890, 1),
    ("Dom Casmurro", "Machado de Assis", 1899, 1),
    ("The Pragmatic Programmer", "David Thomas", 1999, 0),
    ("Memórias Póstumas", "Machado de Assis", 1881, 1),
])

conn.commit()
conn.close()

print("Banco populado com sucesso!")