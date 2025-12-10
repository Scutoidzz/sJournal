import sqlite3 as sql
import sys
import os
import time

cursor = sql.connect()
osname = os.name

def init_db(dbpath):
    try:
        sql.init()
        print(f"easydb: Successfully initialized database at {dbpath}")
    except sql.Error as errmsg:
        print(f"easydb: Error initializing database: {errmsg}")
    
def create_db(dbname, flags):
    print(f"creating database: {dbname}")
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, title TEXT, content TEXT, mood TEXT, rating INTEGER)")
        print(f"easydb: Successfully created database at {dbname}")
        time.sleep(5)
        if os.name == "posix":
            sys.command("clear")
        else:
            sys.command("cls")
    except sql.Error as errmsg:
        #TODO: Add better error handling for certain codes
        print(f"easydb: Error creating database: {errmsg}. pass retry[1-3] to add retries") 
 


