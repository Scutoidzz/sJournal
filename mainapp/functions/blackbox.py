import requests
import os
from pydantic import BaseModel, Field

def get_gemini(prompt):
    apikey = os.getenv("GEMINI_API_KEY")
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?api_key={apikey}"

    class moods(BaseModel):
        mood: str = Field(description="The mood of the day")
        one_to_ten: int = Field(description="the mood score from 1-10")
    # IMPROVEMENT: Define Pydantic models outside of functions to avoid redefining them on every call.
    # This improves performance and code readability.
        
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
            "temperature": 0.8,
            "maxOutputTokens": 64,
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
    
    # FIX: The function constructs the request body but never actually sends the request!
    # You need to add:
    # response = requests.post(gemini_url, json=request_body)
    # response = requests.post(gemini_url, json=request_body)
    # TODO: Uncomment the request line and handle potential network errors (try-except block).
    response = requests.post(gemini_url, json=request_body)
    if response.status_code == 200:
        parse_response(response)
    else:
        print(f"Error: {response.status_code} - {response.text}")

def parse_response(gemini_response):
    print("parse_response started")
    print(f"Output = {gemini_response.json()}")
