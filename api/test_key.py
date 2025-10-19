import os
import json

def handler(request):
    API_KEY = os.getenv("API_KEY")
    return {
        "statusCode": 200,
        "body": json.dumps({"api_key": API_KEY})
    }