import json
import os
import dotenv
import sys
from PyQt6.QtWidgets import QApplication
from mainapp import homescreen
from apisetter import main

dotenv.load_dotenv()

app = QApplication(sys.argv)

main_window = homescreen.homescreen(app, os.getenv("GEMINI_API_KEY"))

if not os.path.exists("config.json"):
    main(app)

# Check if the user has API in their ENV
if not os.getenv("GEMINI_API_KEY"):
    check1 = 0
else: 
    check1 = 1

# Check if config.json exists, if not create it
if not os.path.exists("config.json") and os.getenv("GEMINI_API_KEY"):
    with open("config.json", "w") as config_file:
        json.dump({}, config_file)
    checks = 0


with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Check if the user has completed the intro/personalization
if not config.get("completed", False):
    from intro import welcome
    welcome.welcomescreen(app, os.getenv("GEMINI_API_KEY"))
    check1 = 0

if check1 == 1:
    homescreen.homescreen(app, os.getenv("GEMINI_API_KEY"))
else:
    main(app)
sys.exit(app.exec())