# config.py

import os

class Config:
    # Gemini API Key
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyCqmDwlmYKVKtYi9H1KWmz53Yvcqfvr0MQ")

    # MongoDB Configuration
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Aniflix:Lipun123@aniflix.q2wina5.mongodb.net/?retryWrites=true&w=majority&appName=Aniflix")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "Ethan")

    # Telegram Bot Config (from my.telegram.org)
    API_ID = int(os.environ.get("API_ID", 24817837))
    API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8086801925:AAFC1H9aum3e3_Ny0J_oYAOBHuqBfYWL1_o")

    # Optional settings
    OWNER_ID = int(os.environ.get("OWNER_ID", 7428552084))  # Telegram user ID
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Gemini_KGC_bot")
