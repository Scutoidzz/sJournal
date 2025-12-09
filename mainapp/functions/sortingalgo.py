import sys
import os
import sqlite3
import json
#REMEMBER: qThread is not needed in this case.
def sort_entries_by_date(entries):
    return sorted(entries, key=lambda x: x[1], reverse=True)

def sort_entries_by_title(entries):
    return sorted(entries, key=lambda x: x[2])

def sort_entries_by_mood(entries):
    return sorted(entries, key=lambda x: x[3])

def user_predictions(entries):
    print("TODO")


