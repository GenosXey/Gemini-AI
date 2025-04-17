# callback.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
import pymongo

# Setup MongoDB client
mongo_client = pymongo.MongoClient(Config.MONGO_URI)
db = mongo_client[Config.MONGO_DB_NAME]
users_collection = db["users"]

# Commande /start
@Client.on_message(filters.command("start") & filters.private)
def start_command(client: Client, message: Message):
    user_id = message.from_user.id
    users_collection.update_one({"_id": user_id}, {"$set": {"username": message.from_user.username}}, upsert=True)
    message.reply_text("👋 Salut ! Je suis un bot propulsé par Gemini. Pose-moi n'importe quelle question !")

# Une commande /id sympa pour tester
@Client.on_message(filters.command("id") & filters.private)
def get_user_id(client: Client, message: Message):
    message.reply_text(f"🆔 Ton ID Telegram est : `{message.from_user.id}`", quote=True)
