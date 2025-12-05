import sys
import os
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QApplication


def main(app):
    print ("API Key App")
    with open("./src/introstyling.qss", "r") as style_file:
        stylesheet = style_file.read()
    window = QWidget()
    window.setStyleSheet(stylesheet)
    layout = QVBoxLayout()
    apitext = QLabel("Set an API key for Gemini")
    apibox = QLineEdit()
    apibutton = QPushButton("Set Key")
    layout.addWidget(apitext)
    layout.addStretch()
    layout.addWidget(apibox)
    layout.addWidget(apibutton)


    # Hoping that this will stop garbage collection
    def set_key():
        print("Attempting to set Key")
        api_key = apibox.text()
        os.environ["GEMINI_API_KEY"] = api_key
        # Optionally save to a file for persistence
        with open(".env", "w") as env_file:
            env_file.write(f"GEMINI_API_KEY={api_key}\n")

    apibutton.clicked.connect(set_key)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
        
    
