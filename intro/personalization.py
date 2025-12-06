import sys
import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QApplication
from PyQt6.QtGui import QIcon, QPalette, QColor
from PyQt6.QtCore import Qt, QSize, QRect
import json

from mainapp.functions.utils import load_stylesheet

def choices(app=None, on_complete=None):
    print("Personalization settings loaded")
    
    window = QWidget()
    # Load initial stylesheet
    load_stylesheet(window)
    
    layout = QVBoxLayout()
    window.setFixedSize(683, 384)
    window.setLayout(layout)
    window.setWindowTitle("Personalization")
    
    colors = QLabel("Choose your accent color")
    colors.setStyleSheet("font-size: 18px; font-weight: bold;")
    color_buttons = []
    selected_color_label = QLabel("No accent selected")

    def update_selection(color_name, hex_code):
        selected_color_label.setText(f"Selected accent: {color_name}")
        # Live preview: update stylesheet with selected color
        load_stylesheet(window, override_color=hex_code)

    color_data = [
        ("Red", "#C04040"), ("Green", "#40C040"), ("Blue", "#4040C0"),
        ("Yellow", "#C0C040"), ("Cyan", "#40C0C0"), ("Magenta", "#C040C0"),
        ("Orange", "#C08040"), ("Purple", "#804080")
    ]

    # Add the colors label to the layout
    layout.addWidget(colors)
    
    # Create a horizontal layout for color buttons
    button_layout = QHBoxLayout()
    
    for name, hex_code in color_data:
        btn = QPushButton()
        btn.setObjectName("colorButton")
        btn.setFixedSize(40, 40)
        btn.setStyleSheet(f"QPushButton#colorButton {{ background-color: {hex_code}; }}")
        btn.setProperty("colorHex", hex_code)
        btn.setProperty("colorName", name)
        btn.setCheckable(True)
        btn.setAutoExclusive(True)
        btn.clicked.connect(lambda checked, n=name, h=hex_code: update_selection(n, h))
        button_layout.addWidget(btn)
        color_buttons.append(btn)

    # Pre-select the first color
    if color_buttons:
        color_buttons[0].click()

    def save_and_continue():
        selected_color = None
        selected_hex = None
        for btn, (name, hex_code) in zip(color_buttons, color_data):
            if btn.isChecked():
                selected_color = name
                selected_hex = hex_code
                break
        
        # Write completion status to config.json
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "..", "config.json")
        config_data = {
            "completed": True,
            "accent_color": selected_color,
            "accent_hex": selected_hex
        }
        
        with open(config_path, "w") as config_file:
            json.dump(config_data, config_file, indent=4)
        
        print(f"Setup complete! Accent color: {selected_color}")
        
        # Close this window and call the completion callback
        window.close()
        if on_complete:
            on_complete()
    
    get_started = QPushButton("Get Started")
    get_started.clicked.connect(save_and_continue)
    
    # Add the button layout to the main layout
    layout.addLayout(button_layout)
    layout.addWidget(selected_color_label)
    layout.addStretch()
    layout.addWidget(get_started)
    
    window.show()
    return window  # Return window to prevent garbage collection


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = choices(app)
    sys.exit(app.exec())
