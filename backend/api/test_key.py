import os
import json

def handler(request):
    # Get your API key from environment variables
    API_KEY = os.getenv("API_KEY")
    
    # Just return it in JSON (for testing only! remove before real use)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "api_key": API_KEY
        })
    }
