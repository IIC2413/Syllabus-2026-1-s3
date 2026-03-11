"""
Crea la base de datos peliculas.db con datos de ejemplo
para el tutorial de Álgebra Relacional ↔ SQL.

IIC2413 — Bases de Datos, 2026-1
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "peliculas.db")


def crear_base():
    # Eliminar si ya existe
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # --- Crear tablas ---
    cur.execute("""
        CREATE TABLE Peliculas (
            id           INTEGER PRIMARY KEY,
            nombre       TEXT NOT NULL,
            anio         INTEGER,
            categoria    TEXT,
            calificacion REAL
        );
    """)

    cur.execute("""
        CREATE TABLE Actores (
            id     INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad   INTEGER
        );
    """)

    cur.execute("""
        CREATE TABLE Actuo_en (
            id_actor    INTEGER REFERENCES Actores(id),
            id_pelicula INTEGER REFERENCES Peliculas(id),
            PRIMARY KEY (id_actor, id_pelicula)
        );
    """)

    # --- Insertar datos ---
    peliculas = [
        (1, "Interstellar", 2014, "Ciencia Ficción", 8.7),
        (2, "The Revenant", 2015, "Drama", 8.0),
        (3, "The Imitation Game", 2014, "Drama", 8.0),
        (4, "Harry Potter y la Piedra Filosofal", 2001, "Fantasía", 7.6),
        (5, "Inception", 2010, "Ciencia Ficción", 8.8),
        (6, "The Wolf of Wall Street", 2013, "Drama", 8.2),
        (7, "Arrival", 2016, "Ciencia Ficción", 7.9),
        (8, "Black Swan", 2010, "Drama", 8.0),
    ]

    actores = [
        (1, "Leonardo DiCaprio", 51),
        (2, "Matthew McConaughey", 56),
        (3, "Benedict Cumberbatch", 49),
        (4, "Daniel Radcliffe", 36),
        (5, "Jessica Chastain", 49),
        (6, "Anne Hathaway", 43),
        (7, "Natalie Portman", 44),
        (8, "Amy Adams", 51),
    ]

    actuo_en = [
        (2, 1),  # McConaughey en Interstellar
        (5, 1),  # Chastain en Interstellar
        (6, 1),  # Hathaway en Interstellar
        (1, 2),  # DiCaprio en The Revenant
        (3, 3),  # Cumberbatch en The Imitation Game
        (4, 4),  # Radcliffe en Harry Potter
        (1, 5),  # DiCaprio en Inception
        (1, 6),  # DiCaprio en Wolf of Wall Street
        (8, 7),  # Adams en Arrival
        (7, 8),  # Portman en Black Swan
        (6, 5),  # Hathaway en Inception (ella también sale, interesante para joins)
    ]

    cur.executemany("INSERT INTO Peliculas VALUES (?,?,?,?,?)", peliculas)
    cur.executemany("INSERT INTO Actores VALUES (?,?,?)", actores)
    cur.executemany("INSERT INTO Actuo_en VALUES (?,?)", actuo_en)

    conn.commit()
    conn.close()
    print(f"Base de datos creada en: {DB_PATH}")
    print(f"  - {len(peliculas)} películas")
    print(f"  - {len(actores)} actores")
    print(f"  - {len(actuo_en)} relaciones actor-película")


if __name__ == "__main__":
    crear_base()
