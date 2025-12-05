
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

from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit
import sys
import os
import json
import sqlite3
from .functions import blackbox
from datetime import datetime
from PyQt6.QtCore import Qt
#TODO: Add apple health style slider for emotions
class newEntryWindow(QWidget):
    def __init__(self):
        super().__init__()
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
        save = QPushButton("Save")
        layout.addWidget(save)
        #TODO: Implement the save logic
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.close)
        layout.addWidget(cancel)
    

    

def new_entry():
    """
    Creates and displays the new journal entry window.
    
    Returns:
        QWidget: The window reference (to prevent garbage collection)
    """
    window = newEntryWindow()
    window.show()
    return window

# TODO: Implement save functionality
# def save_entry(title_widget, content_widget, window):
#     """
#     Saves the journal entry to a JSON file.
#     
#     Consider:
#     - Validating that title and content aren't empty
#     - Adding timestamp automatically
#     - Storing entries in a list in entries.json
#     - Showing success/error message with QMessageBox
#     """
#     entry_data = {
#         "title": title_widget.text(),
#         "content": content_widget.toPlainText(),
#         "timestamp": datetime.now().isoformat(),
#     }
#     
#     # Load existing entries, add new one, save back
#     # entries = []
#     # if os.path.exists("entries.json"):
#     #     with open("entries.json", "r") as f:
#     #         entries = json.load(f)
#     # entries.append(entry_data)
#     # with open("entries.json", "w") as f:
#     #     json.dump(entries, f, indent=4)
#     pass

