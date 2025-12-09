import requests
import os
import sqlite3
import json
#TODO: Make this save directly to the database

from pydantic import BaseModel, Field

def get_gemini(prompt):
    #TODO; 
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
                "required": ["one_to_ten"]
            }
        }
    }
    
    # FIX: The function constructs the request body but never actually sends the request!
    # You need to add:
    # response = requests.post(gemini_url, json=request_body)
    # TODO: Uncomment the request line and handle potential network errors (try-except block).
    response = requests.post(gemini_url, json=request_body)
    if response.status_code == 200:
        return parse_response(response)
    else:
        print(f"Error: {response.status_code} - {response.text}")

def parse_response(gemini_response):
    errormessage = "Something went wrong."
    print("parse_response started")
    print(f"Output = {gemini_response.json()}")
    try:
        # Extract the text content from the Gemini response
        response_data = gemini_response.json()
        if 'candidates' in response_data and response_data['candidates']:
            text_content = response_data['candidates'][0]['content']['parts'][0]['text']
            # Parse the JSON string contained in the text
            parsed_content = json.loads(text_content)
            rating = parsed_content.get("one_to_ten")
            mood = parsed_content.get("mood")
            print(f"rating = {rating}, mood = {mood}")
            return {"rating": rating, "mood": mood}
        else:
            print("No candidates found in response")
            return errormessage
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")
        return None
