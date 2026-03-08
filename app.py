from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message")

    response = requests.post(RASA_URL, json={
        "sender": "user",
        "message": user_message
    })

    responses = response.json()

    bot_messages = []

    for r in responses:
        if "text" in r:
            bot_messages.append(r["text"])

    return jsonify({"reply": bot_messages})

if __name__ == "__main__":
    app.run(debug=True)