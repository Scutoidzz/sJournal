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
    toplayout.addWidget(aibutton)
    
    bottomlayout = QHBoxLayout()
    about = QPushButton("About")
    bottomlayout.addWidget(about)

    align = QVBoxLayout()
    align.addLayout(toplayout)
    align.addLayout(bottomlayout)
    layout.addLayout(align)

    window.show()
    return window

    