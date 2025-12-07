import json
from datetime import datetime
from .blackbox import get_gemini
from ..database import add_entry

def compile_entry(content, manual_mood=None):
    ai_analysis = get_gemini(content)
    
    compiled_entry = {
        "content": content,
        "timestamp": datetime.now().isoformat(),
        "ai_analysis": ai_analysis if ai_analysis else {},
        "manual_mood": manual_mood,
        "entry_metadata": {
            "word_count": len(content.split()),
            "character_count": len(content),
            "has_manual_mood": manual_mood is not None
        }
    }
    
    final_mood = manual_mood
    if not final_mood and ai_analysis:
        final_mood = ai_analysis.get("mood")
    
    rating = None
    if ai_analysis:
        rating = ai_analysis.get("one_to_ten")
    
    return {
        "compiled_data": compiled_entry,
        "final_mood": final_mood,
        "rating": rating
    }

def save_compiled_entry(content, manual_mood=None):
    try:
        entry_data = compile_entry(content, manual_mood)
        
        add_entry(
            content=content,
            mood=entry_data["final_mood"],
            rating=entry_data["rating"]
        )
        
        save_compiled_data_backup(entry_data["compiled_data"])
        
        return True
        
    except Exception as e:
        print(f"Error saving compiled entry: {e}")
        return False

def save_compiled_data_backup(compiled_data):
    try:
        import os
        backup_dir = "entry_backups"
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{backup_dir}/entry_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(compiled_data, f, indent=2)
            
    except Exception as e:
        print(f"Error saving backup: {e}")


