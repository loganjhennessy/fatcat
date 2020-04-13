import pickle
import sqlite3

import requests

from fatcat.config import config

sqlite3.register_converter("pickle", pickle.loads)
sqlite3.register_adapter(requests.Response, pickle.dumps)
conn = None


def get_db_conn():
    global conn
    if not conn:
        conn = sqlite3.connect(config.dbpath, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
    return conn
