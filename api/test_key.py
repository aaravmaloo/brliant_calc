import os
import json

# This is the handler Vercel expects for Python serverless functions
def handler(request):
    # Get your API key from Vercel environment variables
    API_KEY = os.getenv("API_KEY")
    
    # Return it in JSON (for testing only — remove later for safety)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "api_key": API_KEY
        })
    }
