from pymongo import MongoClient
from config.settings import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["cyber_threat_db"]
collection = db["threat_intelligence"]

from pymongo import MongoClient

def insert_data(data):
    """Inserts scraped data into MongoDB."""
    try:
        client = MongoClient("mongodb://localhost:27017")  # Update your MongoDB URI as needed
        db = client["cyber_threats_db"]  # Update your database name
        collection = db["threat_intelligence"]  # The collection where data will be stored
        
        # Insert multiple records
        collection.insert_many(data)
        
        print(f"Successfully inserted {len(data)} records into the database.")
    except Exception as e:
        print(f"Error inserting data into MongoDB: {e}")


def get_all_data():
    return list(collection.find({}, {"_id": 0}))
