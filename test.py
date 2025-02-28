from pymongo import MongoClient
from config import MONGO_CONFIG

try:
    client = MongoClient(MONGO_CONFIG["MONGO_URI"])
    db = client[MONGO_CONFIG["DB_NAME"]]
    print("✅ MongoDB Connection Successful!")
    print("Available Collections:", db.list_collection_names())

except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")
