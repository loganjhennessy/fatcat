import sqlite3

from fatcat.config import config

def db_connect():
    conn = sqlite3.connect(config.dbpath)
    yield conn
    conn.close()