from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QSlider
from PyQt6.QtGui import QIcon, QPalette, QColor
from PyQt6.QtCore import Qt, QSize, QRect
from .functions.blackbox import get_gemini
import pygame as pyg
import sys
import csv
import os


def moodpicker():
    print("Mood Picker loading.")
    window = QWidget()
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
    
    moodslider.valueChanged.connect(lambda value: print(f"Mood: {value}"))
    window.show()
    #TODO: Find out if the window is being garbage collected
    return window
    