from PyQt6.QtWidgets import QSpacerItem, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QImage, QFont
import os
import sys

osname = os.name

print(osname)

def abt_window():
    print("Initializing about window")
    window = QWidget()
    layout = QVBoxLayout
    window.setLayout(layout)
    window.setFixedSize(120, 240)
    window.setWindowTitle("About (sJournal)")
    # FONTS
    smallfont = QFont("Arial", 10)
    mediumfont = QFont("Arial", 12)
    largefont = QFont("Arial", 16)
    # COMPONENTS
    aboutname = QLabel("About")
    aboutblurb = QLabel("sJournal")
    aboutversion = QLabel("0.16")
    # CONFIGURE COMPONETS
    aboutname.setFont(largefont)
    aboutblurb.setFont(mediumfont)
    aboutversion.setFont(smallfont)
    # ADD WIDGETS
    layout.addWidget(aboutname)
    spacer = QSpacerItem
    layout.addWidget(spacer)
    layout.addWidget(aboutblurb)
    layout.addWidget(aboutversion)