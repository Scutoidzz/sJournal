from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
import sys
import os
import json

def settings():
    window = QWidget()
    layout = QVBoxLayout()
    window.setLayout(layout)
    window.setFixedSize(683, 384)
    window.setWindowTitle("Settings")
    layout.addStretch()

    toplayout = QHBoxLayout()
    aibutton = QPushButton("AI")
    # FIX: This button is not connected to any function.
    toplayout.addWidget(aibutton)
    
    bottomlayout = QHBoxLayout()
    about = QPushButton("About")
    # FIX: This button is not connected to any function.
    bottomlayout.addWidget(about)

    align = QVBoxLayout()
    align.addLayout(toplayout)
    align.addLayout(bottomlayout)
    layout.addLayout(align)

    window.show()
    return window

    