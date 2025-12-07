import sys
import os
from datetime import datetime
from PyQt6.QtWidgets import  QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
from .newentry import new_entry
from settings.settings import settings
from .database import fetch_entries, init_db
from .functions.utils import load_stylesheet

def homescreen(app, apikey):
    # IMPROVEMENT: Refactor into a class `HomeScreen(QWidget)` to better manage state and methods.
    # Passing `app` and `apikey` around is fine, but a class structure is more idiomatic for main windows.
    init_db()
    window = QWidget()
    layout = QVBoxLayout()
    
    # Load stylesheet with dynamic accent color
    load_stylesheet(app)

    print("Home screen loaded")
    
    window.setLayout(layout)
    window.setFixedSize(683, 384)
    window.setWindowTitle("Home")
    
    
    
    content_widget = QWidget()
    content_layout = QVBoxLayout(content_widget)
    content_layout.setSpacing(15)
    content_layout.setContentsMargins(20, 20, 20, 20)
    
    # Fetch and display entries
    try:
        # IMPROVEMENT: Fetching entries synchronously on the main thread can freeze the UI if the DB is large.
        # Consider using a background thread (QThread) or async/await if possible for DB operations.
        entries = fetch_entries()
        if not entries:
            empty_label = QLabel("A whole lot of nothing going on (click +)")
            empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            content_layout.addWidget(empty_label)
        else:
            for entry in entries:
                card = QFrame()
                card.setObjectName("EntryCard")
                card_layout = QVBoxLayout(card)
                
                # Header (Date + Mood)
                header_layout = QHBoxLayout()
                
                # Parse timestamp
                timestamp_str = entry['timestamp']
                try:
                    dt = datetime.fromisoformat(timestamp_str)
                    date_str = dt.strftime("%B %d, %Y %I:%M %p")
                except ValueError:
                    date_str = timestamp_str
                    
                date_label = QLabel(date_str)
                date_label.setObjectName("DateLabel")
                header_layout.addWidget(date_label)
                
                if entry['mood']:
                    mood_label = QLabel(entry['mood'])
                    mood_label.setObjectName("MoodLabel")
                    mood_label.setAlignment(Qt.AlignmentFlag.AlignRight)
                    header_layout.addWidget(mood_label)
                    
                card_layout.addLayout(header_layout)
                
                content_label = QLabel(entry['content'])
                content_label.setObjectName("ContentLabel")
                content_label.setWordWrap(True)
                card_layout.addWidget(content_label)
                
                content_layout.addWidget(card)
    except Exception as e:
        print(f"Error fetching entries: {e}")
        error_label = QLabel(f"Error loading entries: {e}")
        content_layout.addWidget(error_label)
        
    content_layout.addStretch()
    scroll_area.setWidget(content_widget)
    layout.addWidget(scroll_area)
    
    # Buttons Layout (Bottom)
    btn_layout = QHBoxLayout()
    
    # Settings Button 
    settings_btn = QPushButton("Settings")
    def settings_window_opener():
        # Store reference to prevent garbage collection
        # NOTE: Attaching attributes to `window` dynamically is a bit hacky.
        # A class-based approach would allow you to store these as instance attributes cleanly.
        window.settings_window = settings()
    settings_btn.clicked.connect(settings_window_opener)
    
    # New Entry Button
    newentry_btn = QPushButton("+")
    def open_new_entry():
        # Store reference to prevent garbage collection
        window.new_entry_window = new_entry()
        # Refresh entries when new entry window closes? 
        # For now, user has to restart or we need a signal.
        # Ideally, we would connect a signal from new_entry_window to refresh this list.
        
    newentry_btn.clicked.connect(open_new_entry)

    btn_layout.addWidget(settings_btn)
    btn_layout.addStretch()
    btn_layout.addWidget(newentry_btn)
    
    layout.addLayout(btn_layout)

    window.show()
    return window
