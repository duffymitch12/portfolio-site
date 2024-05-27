import sqlite3
from flask import g

DATABASE = "/Users/mitchellduffy/Desktop/new_site_JSX_FLASK/database/exp.sqlite3"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
