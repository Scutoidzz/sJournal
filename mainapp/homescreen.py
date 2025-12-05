import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from .newentry import new_entry

def homescreen(app, apikey):
    window = QWidget()
    layout = QVBoxLayout()
    # Load stylesheet using absolute path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(script_dir, "..", "src", "introstyling.qss")
    with open(qss_path, "r") as style_file:
        app.setStyleSheet(style_file.read())
    print("Home screen loaded")
    
    window.setLayout(layout)
    window.setFixedSize(683, 384)
    window.setWindowTitle("Home")
    layout.addStretch()
    
    newentry_btn = QPushButton("+")
    def open_new_entry():
        # Store reference to prevent garbage collection
        window.new_entry_window = new_entry()

    newentry_btn.clicked.connect(open_new_entry)
    
    layout.addWidget(newentry_btn)
    window.show()
    return window  # Return window to prevent garbage collection
