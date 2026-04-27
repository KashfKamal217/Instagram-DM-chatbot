import os
from groq import Groq

RESPONSES = {

    "greeting": (
        "Hi, welcome to ZAIQA.\n\n"
        "I can assist you with the following:\n"
        "  - Menu and food items\n"
        "  - Pricing\n"
        "  - Delivery zones and timings\n"
        "  - Table reservations\n"
        "  - Opening hours\n"
        "  - Payment options\n"
        "  - Order tracking\n"
        "  - Current deals\n\n"
        "Type your question and I will respond shortly."
    ),

    "menu": (
        "ZAIQA Full Menu:\n\n"
        "Desi Mains\n"
        "  Karahi, Nihari, Haleem, Sajji\n"
        "  PKR 800 - 2,500\n\n"
        "Grills and BBQ\n"
        "  Seekh Kebab, Chicken Tikka, Malai Boti\n"
        "  PKR 600 - 1,800\n\n"
        "Burgers and Wraps\n"
        "  Zaiqa Special Burger, Crispy Wrap, Club Sandwich\n"
        "  PKR 400 - 900\n\n"
        "Rice Dishes\n"
        "  Biryani, Pulao, Fried Rice\n"
        "  PKR 350 - 1,200\n\n"
        "Deals and Combos\n"
        "  Family Deal, Couple Deal, Student Special\n"
        "  PKR 1,200 - 4,500\n\n"
        "Beverages and Desserts\n"
        "  Lassi, Shakes, Zarda, Gulab Jamun\n"
        "  PKR 150 - 500\n\n"
        "For questions about a specific item, just ask."
    ),

    "pricing": (
        "ZAIQA Pricing:\n\n"
        "Desi Mains           PKR 800  - 2,500\n"
        "Grills and BBQ       PKR 600  - 1,800\n"
        "Burgers and Wraps    PKR 400  - 900\n"
        "Rice Dishes          PKR 350  - 1,200\n"
        "Deals and Combos     PKR 1,200 - 4,500\n"
        "Beverages/Desserts   PKR 150  - 500\n\n"
        "Orders above PKR 1,500 qualify for free delivery.\n"
        "Ask us for the exact price of any specific item."
    ),

    "delivery": (
        "ZAIQA Delivery:\n\n"
        "Lahore, Karachi, Islamabad  -  30 to 45 minutes\n"
        "All other areas             -  60 to 90 minutes\n\n"
        "Delivery charge: PKR 100 (flat)\n"
        "Free delivery on orders above PKR 1,500.\n\n"
        "A tracking update is sent via WhatsApp once your order is dispatched.\n"
        "If you want to confirm delivery to your city, share your location."
    ),

    "reservation": (
        "ZAIQA Table Reservations:\n\n"
        "Available for groups of 2 to 20 people.\n"
        "Bookings must be made at least 2 hours in advance.\n"
        "Confirm via DM or direct call.\n\n"
        "Groups above 10 people require an advance deposit.\n\n"
        "Send us a DM with your preferred date, time, and party size to proceed."
    ),

    "hours": (
        "ZAIQA Opening Hours:\n\n"
        "Monday - Thursday    12:00 PM to 12:00 AM\n"
        "Friday               1:00 PM  to  1:00 AM\n"
        "Saturday - Sunday    11:00 AM to  1:00 AM"
    ),

    "payment": (
        "ZAIQA Payment Options:\n\n"
        "  - JazzCash\n"
        "  - EasyPaisa\n"
        "  - Bank Transfer\n"
        "  - Debit / Credit Card\n"
        "  - Cash on Delivery (COD)\n\n"
        "COD is available in all major cities across Pakistan."
    ),

    "deals": (
        "ZAIQA Deals:\n\n"
        "New deals are posted every Monday.\n\n"
        "Current combos:\n"
        "  Family Deal, Couple Deal, Student Special\n"
        "  PKR 1,200 - 4,500\n\n"
        "Follow @zaiqaeats on Instagram and turn on notifications.\n"
        "Join our WhatsApp broadcast to get deals before they go public."
    ),

    "order_status": (
        "To check your order status, please provide one of the following:\n\n"
        "  - Order ID (from your confirmation message)\n"
        "  - Registered phone number\n\n"
        "A WhatsApp tracking update is sent automatically after dispatch.\n"
        "Share your details here and we will check the status for you."
    ),

    "fallback": (
        "Thank you for contacting ZAIQA.\n\n"
        "We have received your message and a team member will follow up with you shortly.\n\n"
        "For a faster response, reach us directly at: @zaiqaeats"
    ),
}


# ==============================================================

KEYWORDS = {
    "greeting": [
        "hi", "hello", "hey", "salam", "assalam", "aoa",
        "good morning", "good evening", "good afternoon",
    ],
    "menu": [
        "menu", "food", "dish", "khaana", "khana", "item",
        "kya hai", "kya milta", "what do you serve", "what food",
        "what items", "available",
    ],
   "pricing": [
    "price", "cost", "how much", "rate", "pkr",
    "rupee", "kitne", "daam", "charges", "expensive", "cheap",
],
    "delivery": [
        "deliver", "delivery", "ship", "home", "ghar", "area",
        "multan", "faisalabad", "peshawar", "rawalpindi",
        "which city", "cities", "location", "deliver to",
    ],
    "reservation": [
        "book", "reserve", "table", "seat", "dine",
        "reservation", "booking", "sit", "party",
    ],
    "hours": [
    "open", "close", "hours", "kab", "timing",
    "band", "schedule", "when", "what time",
],
    "payment": [
        "pay", "payment", "jazzcash", "easypaisa", "cod",
        "cash", "card", "bank", "transfer", "online pay", "how to pay",
    ],
    "deals": [
        "deal", "discount", "offer", "combo", "special",
        "promo", "sale", "package", "sasta", "today offer",
    ],
    "order_status": [
        "order", "track", "status", "where is", "kitna time",
        "my order", "not arrived", "late", "order id", "tracking",
    ],
}



def get_response(message: str) -> str:
    """
    Receives a raw customer message string.
    Lowercases and strips the message.
    Iterates through KEYWORDS to find a matching topic.
    Returns the corresponding reply from RESPONSES.
    Returns the fallback reply if no keyword matches.
    """
    text = message.lower().strip()

    for topic, keywords in KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return RESPONSES[topic]

    return RESPONSES["fallback"]



SYSTEM_PROMPT = """
You are the customer support assistant for ZAIQA, a Pakistani restaurant.
Your job is to answer customer questions accurately using only the information below.
Reply in plain, professional English. Keep replies concise (under 6 lines).
Do not make up any information. If unsure, direct the customer to @zaiqaeats.

MENU AND PRICES:
- Desi Mains (Karahi, Nihari, Haleem, Sajji): PKR 800 - 2,500
- Grills and BBQ (Seekh Kebab, Chicken Tikka, Malai Boti): PKR 600 - 1,800
- Burgers and Wraps (Zaiqa Special Burger, Crispy Wrap, Club Sandwich): PKR 400 - 900
- Rice Dishes (Biryani, Pulao, Fried Rice): PKR 350 - 1,200
- Deals and Combos (Family Deal, Couple Deal, Student Special): PKR 1,200 - 4,500
- Beverages and Desserts (Lassi, Shakes, Zarda, Gulab Jamun): PKR 150 - 500

OPENING HOURS:
- Monday to Thursday: 12:00 PM - 12:00 AM
- Friday: 1:00 PM - 1:00 AM
- Saturday and Sunday: 11:00 AM - 1:00 AM

DELIVERY:
- Lahore, Karachi, Islamabad: 30 to 45 minutes
- All other areas: 60 to 90 minutes
- Delivery charge: PKR 100. Free on orders above PKR 1,500.

PAYMENT: JazzCash, EasyPaisa, Bank Transfer, Debit/Credit Card, Cash on Delivery.
COD available in all major cities.

RESERVATIONS: Tables for 2 to 20 people. Book at least 2 hours in advance.
Deposit required for groups above 10. Confirm via DM or call.

DEALS: Updated every Monday. Follow @zaiqaeats. WhatsApp broadcast for early access.

ORDER TRACKING: WhatsApp update sent after dispatch.
Customer must provide order ID or registered phone number.

CANCELLATIONS: Cancel within 5 minutes online. Call directly for urgent changes.

If the question is outside the above information, say the team will follow up and mention @zaiqaeats.
"""


def get_response_groq(message: str) -> str:
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            max_tokens=200,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message},
            ],
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Groq Error:", e)
        return "Sorry, I’m having trouble responding right now. Please try again later or contact @zaiqaeats."