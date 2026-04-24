import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Environment variables (secure handling)
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")


# -----------------------------------------
# Webhook Route
# -----------------------------------------
@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # ---------------------------
    # 1. VERIFY WEBHOOK (GET)
    # ---------------------------
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print(" Webhook Verified")
            print("Token matched successfully")
            return challenge, 200
        else:
            print(" Verification failed")
            return "Verification failed", 403

    # ---------------------------
    # 2. RECEIVE MESSAGES (POST)
    # ---------------------------
    elif request.method == "POST":
        data = request.get_json()

        print(" Incoming Data:", data)

        if data.get("object") == "instagram":
            for entry in data.get("entry", []):
                for messaging in entry.get("messaging", []):

                    sender_id = messaging["sender"]["id"]

                    # Ignore bot echo messages
                    if messaging.get("message") and not messaging["message"].get("is_echo"):

                        user_message = messaging["message"].get("text")

                        if user_message:
                            print("👤 User ID:", sender_id)
                            print("💬 Message:", user_message)

        return jsonify({"status": "received"}), 200


# -----------------------------------------
# Home Route
# -----------------------------------------
@app.route("/")
def home():
    return "ZAIQA Bot Running ", 200


# -----------------------------------------
# Run Server
# -----------------------------------------
if __name__ == "__main__":
    app.run(port=5000, debug=True)