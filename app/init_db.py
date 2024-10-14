import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")
DB_PATH = os.path.join(BASE_DIR, "app.sqlite")

def init_db():
    if os.path.exists(DB_PATH):
        return

    with open(SCHEMA_PATH, "r") as f:
        schema = f.read()
        conn = sqlite3.connect(DB_PATH)
        conn.executescript(schema)
        conn.commit()
        conn.close()
