import sqlite3
import os
from datetime import datetime

DB_NAME = "journal.db"
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), DB_NAME)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS journal_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            mood TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_entry(content, mood=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute('INSERT INTO journal_entries (content, timestamp, mood) VALUES (?, ?, ?)',
                   (content, timestamp, mood))
    conn.commit()
    conn.close()

def fetch_entries():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM journal_entries ORDER BY timestamp DESC')
    entries = cursor.fetchall()
    conn.close()
    return entries
