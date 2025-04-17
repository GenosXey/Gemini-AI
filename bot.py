# bot.py

from pyrogram import Client
from config import Config
import callback  # Assure que les handlers soient enregistrés
import os

PORT = int(os.environ.get("PORT", 8080))

app = Client(
    name="gemini_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

if __name__ == "__main__":
    print(f"🤖 Bot démarrage sur le port {PORT}...")
    app.run()
    print("✅ Bot arrêté.")
