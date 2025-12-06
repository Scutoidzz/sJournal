import sys
import os
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QApplication

# The setup DOES call this. Do NOT delete!
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
        with open(".env", "w") as env_file:
            env_file.write(f"GEMINI_API_KEY={api_key}\n")
        
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
