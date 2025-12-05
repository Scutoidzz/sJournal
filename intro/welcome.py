from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
import sys
import os
from .personalization import choices

def welcomescreen(app):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to sJournal, then into src/introstyling.qss
    qss_path = os.path.join(script_dir, "..", "src", "introstyling.qss")
    with open(qss_path, "r") as style_file:
        app.setStyleSheet(style_file.read())
    window = QWidget()
    layout = QVBoxLayout()
    window.setFixedSize(683, 384)
    window.setLayout(layout)
    window.setWindowTitle("Welcome to sJournal")
    layout.addStretch()

    personalization_window = None
    
    def open_personalization():
        nonlocal personalization_window
        personalization_window = choices()
    
    next_btn = QPushButton("Next")
    next_btn.clicked.connect(open_personalization)
    

    layout.addWidget(next_btn)
    window.show()
    return window  # Return to prevent garbage collection

if __name__ == "__main__":
    welcomescreen()
    


