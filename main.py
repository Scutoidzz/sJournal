import json
import os
import dotenv
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette
from PyQt6.QtCore import QObject, pyqtSignal
#TODO: Change the QSS theming. This current theme looks vibe coded and is annoying
dotenv.load_dotenv()

class AppController(QObject):
    """Controls screen transitions throughout the app lifecycle."""
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.current_window = None
        
        # Ensure config.json exists
        if not os.path.exists("config.json"):
            with open("config.json", "w") as config_file:
                json.dump({"completed": False}, config_file)
        
        # Load config
        with open("config.json", "r") as config_file:
            self.config = json.load(config_file)
        
        # Start the appropriate screen
        self.determine_initial_screen()
    
    def determine_initial_screen(self):
        """Determine and show the initial screen based on app state."""
        # If setup is not complete, start the full setup flow
        if not self.config.get("completed", False):
            self.show_welcome()
            return

        # If setup is complete, check for API key
        has_api_key = bool(os.getenv("GEMINI_API_KEY"))
        if not has_api_key:
            # Show API setter, then go to homescreen
            self.show_api_setter(next_screen=self.show_homescreen)
        else:
            self.show_homescreen()
    
    def close_current_window(self):
        """Safely close the current window."""
        if self.current_window:
            self.current_window.close()
            self.current_window = None
    
    def show_welcome(self):
        """Show the welcome screen."""
        from intro import welcome
        self.close_current_window()
        # After welcome, go to API setter as part of setup flow
        self.current_window = welcome.welcomescreen(self.app, on_complete=self.show_api_setter_in_setup)
    
    def show_api_setter_in_setup(self):
        """Show API setter as part of the setup flow."""
        # After API setter, go to personalization
        self.show_api_setter(next_screen=self.show_personalization)

    def show_api_setter(self, next_screen):
        """Show the API key setter screen."""
        from apisetter import main as apisetter
        self.close_current_window()
        
        def on_complete():
            # Reload the env to get the new API key
            dotenv.load_dotenv()
            next_screen()
            
        self.current_window = apisetter(self.app, on_complete=on_complete)
    
    def show_personalization(self):
        """Show the personalization screen."""
        from intro import personalization
        self.close_current_window()
        self.current_window = personalization.choices(self.app, on_complete=self.on_setup_complete)
    
    def on_setup_complete(self):
        """Callback when initial setup is complete."""
        # Reload config to get any changes
        with open("config.json", "r") as config_file:
            self.config = json.load(config_file)
        self.show_homescreen()
    
    def show_homescreen(self):
        """Show the main homescreen."""
        from mainapp import homescreen
        self.close_current_window()
        self.current_window = homescreen.homescreen(self.app, os.getenv("GEMINI_API_KEY"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController(app)
    sys.exit(app.exec())