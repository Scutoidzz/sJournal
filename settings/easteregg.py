from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFrame, QMessageBox
import os
import sys
import pygame
import dotenv
import requests

#TODO: Implement Easter Egg

def easteregg():
    window = QWidgetyout()
    layout = QVBoxLayout()
    window.setLayout(layout)
    window.setFixedSize(300, 300)
    window.setWindowTitle("TUFF GAEM")
    window.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    found = QMessageBox()
    found.setText("egg!")
    found.setStandartButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.TakeMeBack)
    found.setButtonText("OK" | "Take me back")
    
    print("You found the egg easter!")
