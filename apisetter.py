import sys
import os
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QApplication

# The setup DOES call this. Do NOT delete!
# IMPROVEMENT: Rename 'main' to something more descriptive like 'create_api_setter_window' or 'ApiSetterWindow'.
# Using 'main' can be confusing as it implies an entry point script.
# IMPROVEMENT: Refactor this into a class (e.g., class ApiSetterWindow(QWidget)) to better manage state
# and event handling, similar to how you might structure other complex windows.
def main(app, on_complete=None):
    print("API Key App")
    from mainapp.functions.utils import load_stylesheet
    window = QWidget()
    load_stylesheet(window)
    layout = QVBoxLayout()
    apitext = QLabel("Set an API key for Gemini")
    apibox = QLineEdit()
    current_key = os.getenv("GEMINI_API_KEY")
    if current_key:
        apibox.setText(current_key)
    apibox.setPlaceholderText("Enter your Gemini API key...")
    apibox.setEchoMode(QLineEdit.EchoMode.Password)  # Hide the API key
    apibutton = QPushButton("Set Key")
    layout.addWidget(apitext)
    layout.addStretch()
    layout.addWidget(apibox)
    layout.addWidget(apibutton)

    def set_key():
        print("Attempting to set Key")
        api_key = apibox.text().strip()
        
        if not api_key:
            apitext.setText("Please enter a valid API key!")
            return
        
        os.environ["GEMINI_API_KEY"] = api_key
        # Save to .env file for persistence
        # FIX: This overwrites the entire .env file! If you have other variables, they will be lost.
        # Consider reading existing content first or using append mode (if appropriate, but be careful of duplicates).
        # IMPROVEMENT: Use a library like `python-dotenv`'s `set_key` function (if available/installed)
        # or manually parse and update the specific key to preserve other environment variables.
        env_path = ".env"
        lines = []
        if os.path.exists(env_path):
            with open(env_path, "r") as env_file:
                lines = env_file.readlines()
        
        # Remove existing GEMINI_API_KEY line if present
        lines = [line for line in lines if not line.strip().startswith("GEMINI_API_KEY=")]
        
        # Append the new key
        lines.append(f"GEMINI_API_KEY={api_key}\n")
        
        with open(env_path, "w") as env_file:
            env_file.writelines(lines)
        
        print("API Key saved successfully!")
        
        # Close this window and call the completion callback
        window.close()
        if on_complete:
            on_complete()

    apibutton.clicked.connect(set_key)
    window.setLayout(layout)
    window.setFixedSize(683, 384)
    window.setWindowTitle("API Key Setup")
    window.show()
    return window  # Return window to prevent garbage collection


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main(app)
    sys.exit(app.exec())
