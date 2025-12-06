
# =============================================================================
# TODO: Remove this large commented-out block once the instructions are implemented or moved to documentation.
# Keeping dead code/instructions in the source file clutters the codebase.
# =============================================================================

from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox
import sys
import os
import json
from .database import init_db, add_entry
from .functions import blackbox
from datetime import datetime
from PyQt6.QtCore import Qt

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
        # FIX: This button is created but not connected to any function.
        # It needs to open a mood picker or toggle a mood input.
        # TODO: Implement mood selection logic.
        layout.addWidget(mood)
        save = QPushButton("Save")
        save.clicked.connect(self.save_entry)
        layout.addWidget(save)
        
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.close)
        layout.addWidget(cancel)
    
    def save_entry(self):
        content = self.entryinput.toPlainText()
        if not content.strip():
            QMessageBox.warning(self, "Empty Entry", "Please write something before saving.")
            return
            
        try:
            # FIX: add_entry expects a 'mood' argument (default is None).
            # You should capture the mood from the UI and pass it here.
            # e.g., add_entry(content, current_mood)
            # TODO: Pass the actual selected mood instead of relying on the default None.
            add_entry(content)
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save entry: {e}")
            print(f"Error saving entry: {e}")

def new_entry():
    """
    Creates and displays the new journal entry window.
    
    Returns:
        QWidget: The window reference (to prevent garbage collection)
    """
    window = newEntryWindow()
    window.show()
    return window

