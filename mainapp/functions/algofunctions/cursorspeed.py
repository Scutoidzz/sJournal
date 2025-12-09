#IDEA: user will move cursor faster when anxious. show them their worst days with the delete button highlighted when this happens.
import time
import threading
import pyautogui
#TODO: import the algorithm and add algorithm functions

#TODO: add the cursor speed detection
class CursorSpeedDetector:
    def __init__(self):
        self.speed_threshold = 500  # pixels per second
        self.speed_history = []
        self.is_anxious = False
    def checker(self):
        if self.speed_history[-1] > self.speed_threshold:
            self.is_anxious = True
        else:
            self.is_anxious = False
    def algo_changer(self):
        print("Changing the algorithm")