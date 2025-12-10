import sqlite3 as sql

def init_db(dbpath):
    print(f"easydb: Initializing SQLite Database: {dbpath}")
    sql.init(dbpath)

def cursor_get():
