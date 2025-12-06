import os
import json
import sys

def load_stylesheet(app_or_widget, override_color=None):
    """
    Loads the stylesheet, replaces the @ACCENT_COLOR placeholder with the 
    user's chosen accent color from config.json (or override_color), and applies it.
    """
    # Determine paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming utils.py is in mainapp/functions/
    # config.json is in the root (../../config.json)
    root_dir = os.path.dirname(os.path.dirname(script_dir))
    config_path = os.path.join(root_dir, "config.json")
    # IMPROVEMENT: Use a centralized Config Manager or constants file for paths.
    # Repeatedly calculating paths based on `__file__` is fragile.
    
    # Stylesheet path (src/introstyling.qss)
    qss_path = os.path.join(root_dir, "src", "introstyling.qss")
    
    # Default accent color
    accent_color = "#4a90d9"
    
    if override_color:
        accent_color = override_color
    elif os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                config = json.load(f)
                loaded_color = config.get("accent_hex")
                if loaded_color:
                    accent_color = loaded_color
        except Exception as e:
            print(f"Error reading config: {e}")
            # IMPROVEMENT: Consider using the logging module instead of print statements for better debugging and control.
            
    # Load and process stylesheet
    if os.path.exists(qss_path):
        try:
            with open(qss_path, "r") as f:
                style_content = f.read()
                
            # Replace placeholder
            style_content = style_content.replace("@ACCENT_COLOR", accent_color)
            
            # Apply stylesheet
            app_or_widget.setStyleSheet(style_content)
            print(f"Stylesheet loaded with accent color: {accent_color}")
        except Exception as e:
            print(f"Error loading stylesheet: {e}")
    else:
        print(f"Stylesheet not found at {qss_path}")
