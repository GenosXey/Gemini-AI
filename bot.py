# bot.py

from pyrogram import Client
from config import Config
import callback  # Assure que les handlers soient enregistrés
import os
from pyrogram.types import Message
from pyrogram import filters
import httpx

PORT = int(os.environ.get("PORT", 8080))

app = Client(
    name="gemini_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Fonction pour interroger l'API Gemini
def ask_gemini(question: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={Config.GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": question}]}]
    }
    try:
        response = httpx.post(url, json=data, headers=headers, timeout=20)
        if response.status_code == 200:
            content = response.json()
            return content['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"Erreur Gemini: {response.status_code}"
    except Exception as e:
        return f"Erreur d'appel à Gemini: {e}"

# Répondre automatiquement à tout texte
@app.on_message(filters.private & filters.text & ~filters.command("start"))
def handle_message(client: Client, message: Message):
    question = message.text.strip()
    reply = ask_gemini(question)
    message.reply_text(reply or "❌ Aucune réponse générée.")

if __name__ == "__main__":
    print(f"🤖 Bot démarrage sur le port {PORT}...")
    app.run()
    print("✅ Bot arrêté.")
