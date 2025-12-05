import sys
import os
# Add parent directory to path for absolute imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication
from PyQt6.QtGui import QIcon, QPalette, QColor
from PyQt6.QtCore import Qt, QSize, QRect
from mainapp.homescreen import homescreen
import json


def choices():
    print("Personalization settings loaded")
    # Load the stylesheet using absolute path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(script_dir, "..", "src", "introstyling.qss")
    with open(qss_path, "r") as style_file:
        stylesheet = style_file.read()
    
    window = QWidget()
    window.setStyleSheet(stylesheet)
    layout = QVBoxLayout()
    window.setFixedSize(683, 384)
    window.setLayout(layout)
    window.setWindowTitle("Personalization")
    colors = QLabel("Accent color")
    color_buttons = []
    selected_color_label = QLabel("No accent selected")

    def update_selection(color_name):
        selected_color_label.setText(f"Selected accent: {color_name}")

    color_data = [
        ("Red", "#FF0000"), ("Green", "#00FF00"), ("Blue", "#0000FF"),
        ("Yellow", "#FFFF00"), ("Cyan", "#00FFFF"), ("Magenta", "#FF00FF"),
        ("Orange", "#FFA500"), ("Purple", "#800080")
    ]

    # Add the colors label to the layout
    layout.addWidget(colors)
    
    # Create a horizontal layout for color buttons
    from PyQt6.QtWidgets import QHBoxLayout
    button_layout = QHBoxLayout()
    
    for name, hex_code in color_data:
        btn = QPushButton()
        btn.setObjectName("colorButton")  # Set object name to distinguish from regular buttons
        btn.setFixedSize(40, 40)
       
        btn.setStyleSheet(f"QPushButton#colorButton {{ background-color: {hex_code}; }}")
        btn.setProperty("colorHex", hex_code)
        btn.setProperty("colorName", name)
        btn.setCheckable(True)
        btn.setAutoExclusive(True) # Ensures only one can be checked at a time
        btn.clicked.connect(lambda checked, n=name: update_selection(n))
        button_layout.addWidget(btn)
        color_buttons.append(btn)

    
    def save_and_continue():
        selected_color = None
        selected_hex = None
        for btn, (name, hex_code) in zip(color_buttons, color_data):
            if btn.isChecked():
                selected_color = name
                selected_hex = hex_code
                break
        
        # Write completion status to config.json
        config_data = {
            "completed": True,
            "accent_color": selected_color,
            "accent_hex": selected_hex
        }
        
        with open("config.json", "w") as config_file:
            json.dump(config_data, config_file, indent=4)
        
        # Open the home screen and store reference
        window.home_window = homescreen()
        
        # Close the personalization window
        window.close()
    
    get_started = QPushButton("Get Started")
    get_started.clicked.connect(save_and_continue)
    
    # Add the button layout to the main layout
    layout.addLayout(button_layout)
    layout.addWidget(selected_color_label)
    layout.addWidget(get_started)
    
    window.show()
    return window  # Return window to prevent garbage collection

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = choices()  # Store reference to prevent garbage collection
    sys.exit(app.exec())
