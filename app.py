import os, psycopg

def get_conn():
    return psycopg.connect(os.environ["DATABASE_URL"])

def add_user(name):
    with get_conn() as c:
        c.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL, name TEXT)")
        c.execute("INSERT INTO users (name) VALUES (%s)", (name,))

def count_users():
    with get_conn() as c:
        return c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
