from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QSlider
from PyQt6.QtGui import QIcon, QPalette, QColor
from PyQt6.QtCore import Qt, QSize, QRect
from functions.blackbox import get_gemini
import pygame as pyg
import sys
import csv
import os


def moodpicker():
    #TODO: Slider button in PyQt6/PyGame if I can...
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
    moodslider.tickPosition(Qt.TickPosition.NoTicks)
    moodslider.setRange(0, 5)
    moodslider.setValue(0)
    moodslider.valueChanged.connect(lambda value: print(f"Mood: {value}"))
    
    window.show()
    