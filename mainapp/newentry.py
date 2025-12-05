
# 2. PATH HANDLING - Add sys.path configuration like in personalization.py:
#    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#    This allows proper imports from other modules (like homescreen.py)
#
# 3. STYLESHEET LOADING - Load your QSS stylesheet for consistent styling:
#    with open("../src/mainstyling.qss", "r") as style_file:
#        window.setStyleSheet(style_file.read())
#
# 4. CONSIDER CREATING A CLASS - Your homescreen.py uses functions, but for
#    more complex screens with state (like saving/editing entries), a class
#    would be better:
#    
#    class NewEntryWindow(QWidget):
#        def __init__(self):
#            super().__init__()
#            self.init_ui()
#        
#        def init_ui(self):
#            # Setup code here
#            pass
#        
#        def save_entry(self):
#            # Save logic here
#            pass
#
# 6. SIGNAL CONNECTIONS - Connect buttons to their handlers properly:
#    - Use lambda functions for passing arguments (see personalization.py line 54)
#    - Remember to store window references to prevent garbage collection
#
# 7. NAVIGATION - Add a way to return to homescreen:
#    - Import homescreen module
#    - Add a "Cancel" or "Back" button
#    - Store reference to new window before closing current
#
# =============================================================================

from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox
import sys
import os
import json
from .database import init_db, add_entry
from .functions import blackbox
from datetime import datetime
from PyQt6.QtCore import Qt

#TODO: Add apple health style slider for emotions
class newEntryWindow(QWidget):
    def __init__(self):
        super().__init__()
        init_db()  # Ensure database exists
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        # Load the stylesheet from QT
        #TODO: Find out how to dynamically update the QSS with an accent color
        script_dir = os.path.dirname(os.path.abspath(__file__))
        qss_path = os.path.join(script_dir, "..", "src", "introstyling.qss")
        with open(qss_path, "r") as style_file:
            self.setStyleSheet(style_file.read())
        self.setLayout(layout)
        self.setFixedSize(683, 384)
        self.setWindowTitle("New Entry")
        layout.addStretch()
        self.entryinput = QTextEdit()
        layout.addWidget(self.entryinput)
        layout.addStretch()
        mood = QPushButton("Mood")
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

