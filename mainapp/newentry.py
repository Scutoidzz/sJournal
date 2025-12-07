from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox
import sys
import os
import json
from .database import init_db, add_entry
from .functions import blackbox
from .functions.save_func import save_compiled_entry
from datetime import datetime
from PyQt6.QtCore import Qt
from .mood import moodpicker
#TODO: pack up the entry into json and then pass it to blackbox, then to the sqlite
#TODO: Add apple health style slider for emotions
from .functions.utils import load_stylesheet

class newEntryWindow(QWidget):
    def __init__(self): 
        super().__init__()
        init_db()  # Ensure database exists
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        # Load the stylesheet from QT
        load_stylesheet(self)
        self.setLayout(layout)
        self.setFixedSize(683, 384)
        self.setWindowTitle("New Entry")
        layout.addStretch()
        self.entryinput = QTextEdit()
        layout.addWidget(self.entryinput)
        layout.addStretch()
        mood = QPushButton("Mood")
        mood.clicked.connect(self.open_mood_picker)
        layout.addWidget(mood)
        save = QPushButton("Save")
        save.clicked.connect(self.save_entry)
        layout.addWidget(save)
        
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.close)
        layout.addWidget(cancel)
    
    def open_mood_picker(self):
        self.mood_window = moodpicker()
        self.mood_window.show()
    
    def save_entry(self):
        content = self.entryinput.toPlainText()
        if not content.strip():
            QMessageBox.warning(self, "Empty Entry", "Please write something before saving.")
            return

        # Get any manually selected mood (if implemented)
        manual_mood = getattr(self, 'selected_mood', None)
            
        try:
            # Use the new compilation logic to save everything as one entry
            success = save_compiled_entry(content, manual_mood)
            
            if success:
                self.close()
            else:
                QMessageBox.critical(self, "Error", "Could not save entry. Please try again.")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save entry: {e}")
            print(f"Error saving entry: {e}")

def new_entry():
    window = newEntryWindow()
    window.show()
    return window

