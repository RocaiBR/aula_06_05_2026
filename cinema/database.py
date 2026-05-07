import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "cinema.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS cinema (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sala (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            numero      INTEGER NOT NULL,
            capacidade  INTEGER NOT NULL,
            cinema_id   INTEGER NOT NULL REFERENCES cinema(id)
        );

        CREATE TABLE IF NOT EXISTS filme (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo        TEXT NOT NULL,
            duracao_min   INTEGER NOT NULL,
            classificacao TEXT,
            ativo         INTEGER NOT NULL DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS sessao (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora      TEXT NOT NULL,
            sala_id        INTEGER NOT NULL REFERENCES sala(id),
            filme_id       INTEGER NOT NULL REFERENCES filme(id),
            valor_ingresso REAL NOT NULL DEFAULT 0.0
        );

        CREATE TABLE IF NOT EXISTS registro_publico (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            sessao_id  INTEGER NOT NULL REFERENCES sessao(id),
            data       TEXT NOT NULL,
            quantidade INTEGER NOT NULL CHECK(quantidade >= 0)
        );
    """)

    # Seed data for demo
    cursor.execute("SELECT COUNT(*) FROM cinema")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO cinema (nome, cidade, estado) VALUES (?, ?, ?)",
                       ("Cine Central", "São Paulo", "SP"))
        cinema_id = cursor.lastrowid

        cursor.execute("INSERT INTO sala (numero, capacidade, cinema_id) VALUES (?, ?, ?)",
                       (1, 120, cinema_id))
        sala_id = cursor.lastrowid

        cursor.execute("INSERT INTO filme (titulo, duracao_min, classificacao, ativo) VALUES (?, ?, ?, ?)",
                       ("O Grande Espetáculo", 110, "12", 1))
        filme_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO sessao (data_hora, sala_id, filme_id, valor_ingresso) VALUES (?, ?, ?, ?)",
            ("2026-05-06 19:30", sala_id, filme_id, 25.0)
        )

    conn.commit()
    conn.close()
