from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")  # your secret ExchangeRate API key

@app.route("/convert")
def convert():
    # Get query parameters from URL
    amount = float(request.args.get("amount", 1))
    from_currency = request.args.get("from", "USD")
    to_currency = request.args.get("to", "INR")

    # Call ExchangeRate API
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    resp = requests.get(url).json()

    # Calculate converted amount
    rate = resp["conversion_rates"].get(to_currency)
    if not rate:
        return jsonify({"error": "Invalid target currency"}), 400

    converted = amount * rate
    return jsonify({
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
        "converted": converted
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))