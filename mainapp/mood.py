from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QSlider
from PyQt6.QtGui import QIcon, QPalette, QColor
from PyQt6.QtCore import Qt, QSize, QRect, QImage
from .functions.blackbox import get_gemini
#REMEMBER: PyGame isn't needed in this case.
import sys
import csv
import os
 
def moodpicker():
    # CRITICAL: This window is not being properly managed and could be garbage collected
    # Consider making it a class that inherits from QWidget and properly manages its lifecycle
    print("Mood Picker loading.")
    window = QWidget()
    window.setStyleSheet("mood.qss")
#   window.setWindowIcon(QIcon("icon.png"))
    layout = QVBoxLayout()
    window.setLayout(layout)
    window.setFixedSize(683, 384)
    window.setWindowTitle("Mood Picker")
    labelformoods = QLabel("Mood Picker")
    layout.addWidget(labelformoods)
    moodslider = QSlider()
    layout.addWidget(moodslider)
    moodslider.setTickPosition(QSlider.TickPosition.TicksBelow)
    moodslider.setRange(0, 5)
    moodslider.setValue(0)
    moodslider.setTickInterval(1)
    #TODO: Make moodslider horizontal
    moodslider.valueChanged.connect(lambda value: print(f"Mood: {value}"))
    
    window.show()
    # CRITICAL: The window is not being properly parented and could be garbage collected
    # Store a reference to this window in the parent or use Qt's memory management
    return window

    