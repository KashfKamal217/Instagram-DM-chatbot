# 🍽️ ZAIQA Instagram DM Automation Bot
### Automating Instagram customer conversations with AI-powered replies for seamless restaurant support.

---

## 📌 Project Overview

ZAIQA Bot is a **Flask-based Instagram DM automation system** for a restaurant.  
It receives customer messages through **Instagram Webhooks**, processes them using a Python backend, and generates intelligent replies using **Groq AI**.

---

## ⚙️ Tech Stack

- Python 3  
- Flask  
- Meta Graph API (Instagram Messaging)  
- requests  
- python-dotenv  
- Groq API (LLaMA 3.1 8B Instant)  

---

## 🚀 Features

- Webhook verification (GET request)  
- Receive Instagram DMs (POST request)  
- Extract sender ID and message text  
- Ignore echo messages (prevents loops)  
- AI-generated replies using Groq  
- Send responses via Meta Graph API  
- Secure environment variables using `.env`  

---

## 📁 Project Structure

```
├── app.py           # Flask server & webhook logic
├── responses.py     # Groq AI response system
├── requirements.txt # Dependencies
├── .env             # Environment variables (not committed)
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
VERIFY_TOKEN=your_verify_token
PAGE_ACCESS_TOKEN=your_page_access_token
GROQ_API_KEY=your_groq_api_key
```

---

## 🔗 Webhook Endpoint

### `/webhook`

Handles:

- **GET** → Verifies webhook with Meta  
- **POST** → Receives incoming Instagram messages  

---

## 🔄 Message Flow

1. User sends a message on Instagram  
2. Meta sends the event to `/webhook`  
3. Flask server processes the request  
4. Extracts:
   - Sender ID  
   - Message text  
5. Message is passed to `get_response()`  
6. Groq AI generates a reply  
7. Reply is sent back via Graph API  

---

## 🧠 Response Logic System

The response system is implemented in `responses.py` using **Groq AI**.

### How it works:

- A **SYSTEM_PROMPT** defines:
  - Restaurant details (menu, pricing, policies, timings)  
  - Tone (friendly, concise, Urdu-English mix)  

- Each user message is sent to the model along with this prompt  
- The model generates a contextual reply  

### Model Configuration:

- Model: `llama-3.1-8b-instant`  
- Max tokens: `200`  

### Fallback Response:

If the API fails:

```
Our team will follow up shortly! You can also reach us at @zaiqaeats
```

---

## 📤 Sending Messages

Handled in `app.py` using:

```
https://graph.facebook.com/v18.0/me/messages
```

- Uses `PAGE_ACCESS_TOKEN`  
- Sends messages via `requests.post()`  

---

## ▶️ Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python app.py
```

Server runs at:

```
http://localhost:5000
```

---

## 🏠 Root Endpoint

```
GET /
```

Response:

```
ZAIQA Bot Running 🚀
```

---

## 📦 Requirements

```
flask
requests
python-dotenv
groq
```

---

## 👨‍💻 Author

ZAIQA Bot Development Team
