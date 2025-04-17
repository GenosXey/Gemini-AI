# db.py

from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DB_NAME]

# Users collection
users = db["users"]

def add_user(user_id: int, username: str):
    users.update_one({"_id": user_id}, {"$set": {"username": username}}, upsert=True)

def get_user(user_id: int):
    return users.find_one({"_id": user_id})

def get_all_users():
    return list(users.find())

def delete_user(user_id: int):
    users.delete_one({"_id": user_id})
