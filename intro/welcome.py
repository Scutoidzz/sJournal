from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
import sys
import os


def welcomescreen(app, on_complete=None):
    from mainapp.functions.utils import load_stylesheet
    load_stylesheet(app)
    
    window = QWidget()
    layout = QVBoxLayout()
    window.setFixedSize(683, 384)
    window.setLayout(layout)
    window.setWindowTitle("Welcome to sJournal")
    
    # Welcome message
    welcome_label = QLabel("Welcome to sJournal!")
    welcome_label.setStyleSheet("font-size: 24px; font-weight: bold;")
    layout.addWidget(welcome_label)
    
    description = QLabel("super underrated journaling app.")
    description.setStyleSheet("font-size: 8px; font-weight: italic;")
    layout.addWidget(description)
    
    layout.addStretch()
    
    def go_to_personalization():
        window.close()
        if on_complete:
            on_complete()
    
    next_btn = QPushButton("Next")
    next_btn.clicked.connect(go_to_personalization)
    
    layout.addWidget(next_btn)
    window.show()
    return window  # Return to prevent garbage collection


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = welcomescreen(app)
    sys.exit(app.exec())
