#IDEA: user will move cursor faster when anxious. show them their worst days with the delete button highlighted when this happens.
import time
import threading
import pyautogui

class CursorSpeedDetector:
    def __init__(self):
        self.speed_threshold = 500  # pixels per second
        self.speed_history = []
        self.is_anxious = False