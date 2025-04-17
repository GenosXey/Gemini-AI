# bot.py

from pyrogram import Client
from config import Config
import callback  # Assure que les handlers soient enregistrés

app = Client(
    name="gemini_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

if __name__ == "__main__":
    print("🤖 Bot démarrage...")
    app.run()
    print("✅ Bot arrêté.")
