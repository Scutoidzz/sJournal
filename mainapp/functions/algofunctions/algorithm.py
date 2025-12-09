from os.path import isfile
import sqlite3
import json
import os
from cursorspeed import CursorSpeedDetector

#TODO: Make this into a social journaling app. I can use JSON to list and show it in the json list.

db_path = os.path.join(os.path.dirname(__file__), "entries.db")
print(f"db_path set: {db_path}")
if os.path.isfile(dbf):
#TODO: Add debugging logs to all of my code
    connector = sqlite3.connect(dbf)
    print("Connector Loaded")

    #TODO: find out how to parse the database file
    cursor = connector.cursor()
    cursor.execute("SELECT * from journal_entries")
    unalgo = cursor.fetchall()
    unalgo_json = unalgo.json()
    #TODO: Add algorithm completed version of the json.


