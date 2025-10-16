from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/me", methods=["GET"])
def get_me():
    # Fetch a random cat fact from catfact.ninja
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        fact_data = response.json()
        cat_fact = fact_data.get("fact", "Cats are awesome!")
    except requests.RequestException:
        cat_fact = "Could not fetch cat fact at the moment."

    # Construct the response
    data = {
        "status": "success",
        "user": {
            "email": "martins.ikwueze@gmail.com",
            "name": "Martins Uchechukwu Ikwueze",
            "stack": "Python/Flask"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",  # ISO 8601 UTC time
        "fact": cat_fact
    }

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)