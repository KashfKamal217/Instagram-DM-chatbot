import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from responses import get_response

load_dotenv()

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")


# -------------------------
# SEND MESSAGE FUNCTION
# -------------------------
def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={ACCESS_TOKEN}"

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }

    res = requests.post(url, json=payload)
    print("Message Sent:", res.status_code, res.text)


# -------------------------
# WEBHOOK
# -------------------------
@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # VERIFY
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Webhook Verified ")
            return challenge, 200

        return "Verification failed", 403

    # RECEIVE MESSAGE
    if request.method == "POST":
        data = request.get_json()
        print("Incoming Webhook Data:", data)

        if data.get("object") == "instagram":

            for entry in data.get("entry", []):
                for messaging in entry.get("messaging", []):

                    sender_id = messaging["sender"]["id"]

                    if messaging.get("message") and not messaging["message"].get("is_echo"):

                        user_message = messaging["message"].get("text")

                        if user_message:
                            print("User:", user_message)

                            reply = get_response(user_message)

                            send_message(sender_id, reply)

        return jsonify({"status": "ok"}), 200


# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():
    return "ZAIQA Bot Running 🚀", 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
