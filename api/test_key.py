import os
import json

def handler(request):
    API_KEY = os.getenv("API_KEY")  # reads Vercel environment variable

    # Always return a proper dict with statusCode, headers, and body
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"api_key": API_KEY or "API_KEY not set"})
    }
