#  Instagram DM Chatbot - ZAIQA Bot

##  Project Overview
This project is a Flask-based Instagram DM automation bot for the ZAIQA restaurant.  
It receives customer messages via Instagram Webhooks and processes them using Python backend logic.

---

## ⚙ Tech Stack
- Python 3
- Flask
- Meta Graph API (Instagram Messaging)
- dotenv (.env for security)

---

##  Features (Current Friday Progress)
- Instagram webhook verification (GET request)
- Message receiving via Instagram DM (POST request)
- Sender ID & message extraction
- Safe handling of bot echo messages
- Environment variable security (.env)

---

##  Environment Variables
Create a `.env` file:

VERIFY_TOKEN=your_verify_token  
PAGE_ACCESS_TOKEN=your_access_token  
INSTAGRAM_ACCOUNT_ID=your_instagram_id  

---

##  Webhook Route
`/webhook`

Handles:
- GET → Webhook verification
- POST → Incoming Instagram messages

---

##  Current Status (Friday Task)
✔ Backend Flask server setup  
✔ Webhook verification working  
✔ Instagram message receiver implemented  
✔ Code pushed to GitHub  

---

##  Next Steps
- Connect ngrok for live testing  
- Add message auto-reply logic  
- Integrate Groq AI response system  
- Full Instagram DM automation  

---

##  Author
ZAIQA Bot Development Team