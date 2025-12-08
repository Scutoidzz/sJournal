import sqlite3
import os
from datetime import datetime
import json
import hashlib
#TODO: COMPLETE REWRITE
import sys
DB_NAME = "sjournal.db"
# IMPROVEMENT: Use a configuration file or environment variable for the database path.
# Hardcoding relative paths can lead to issues if the script is run from a different directory.
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), DB_NAME)

def get_db_connection():
    # CRITICAL: No connection pooling or connection management
    # Consider using a connection pool or context managers for better resource management
    try:
            conn = sqlite3.connect(DB_PATH)
            # CRITICAL: No error handlingfor database connection failures
            conn.row_factory = sqlite3.Row
            return conn
    except:
            print("Database connection failed")

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

def add_entry(content, mood=None, rating=None):
    # CRITICAL: No input validation for content or mood
    # CRITICAL: Rating parameter is accepted but not used in the query
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    # CRITICAL: Storing timestamps as ISO strings makes date-based queries difficult
    # Consider using INTEGER for timestamps (UNIX timestamp) or SQLite's built-in datetime functions
    cursor.execute('INSERT INTO journal_entries (content, timestamp, mood) VALUES (?, ?, ?)',
                   (content, timestamp, mood))
    conn.commit()
    conn.close()

def fetch_entries():
    # CRITICAL: No error handling for database operations
    # CRITICAL: No limit on the number of entries returned - could cause memory issues
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM journal_entries ORDER BY timestamp DESC')
    # CRITICAL: Consider adding pagination or limiting results
    # CRITICAL: No transaction management for read operations
    entries = cursor.fetchall()
    conn.close()
    return entries
