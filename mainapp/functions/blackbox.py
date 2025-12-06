import requests
import os
from pydantic import BaseModel, Field


def get_gemini(prompt):
    apikey = os.getenv("GEMINI_API_KEY")
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?api_key={apikey}"

    class moods(BaseModel):
        mood: str = Field(description="The mood of the day")
        one_to_ten: int = Field(description="the mood score from 1-10")
        
    request_body = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.9,
            "maxOutputTokens": 2048,
            "responseMimeType": "application/json",
            "responseSchema": {
                "type": "object",
                "properties": {
                    "mood": {
                        "type": "string",
                        "description": "The mood of the day"
                    },
                    "one_to_ten": {
                        "type": "integer",
                        "description": "The mood score from 1-10"
                    }
                },
                "required": ["mood", "one_to_ten"]
            }
        }
    }
