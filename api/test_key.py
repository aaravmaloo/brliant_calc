import os
import json

def handler(request, response):
    # Get API key from environment
    API_KEY = os.getenv("API_KEY")

    # If API_KEY is missing, return a message
    if not API_KEY:
        response.status_code = 500
        return {"error": "API_KEY not set in environment variables"}

    # Return the key (for testing only)
    response.status_code = 200
    return {"api_key": API_KEY}
