import joblib
from .model_utils import vectorizer
import pandas as pd
from pymongo import MongoClient
import json
import os
from datetime import datetime
import numpy as np

# Load trained models
classifier = joblib.load("ai_model/classifier_model.pkl")
predictor = joblib.load("ai_model/predictor_model.pkl")
profiler = joblib.load("ai_model/profiler_model.pkl")

# MongoDB Connection Setup
MONGO_URI = os.getenv("MONGO_URI")  # Use environment variable for security
DB_NAME = "cyber_threats_db"  # Your MongoDB database name

# Function to fetch data from MongoDB
def fetch_all_data_from_mongo():
    """Fetch all description, title, and date from MongoDB."""
    with MongoClient(MONGO_URI) as client:
        db = client[DB_NAME]
        collection = db['threat_intelligence']  # Collection where your threat data is stored

        # Fetch all documents from the collection
        entries = collection.find({}, {"_id": 0, "description": 1, "title": 1, "date": 1, "url": 1})

        # Return a list of dictionaries containing description, title, date, and url
        return list(entries)

def make_predictions(input_text, title, input_date):
    """Function to predict based on input description, title, and date."""
    
    # Input text for classification (description)
    X_text = vectorizer.transform([input_text])
    predicted_class = classifier.predict(X_text)[0]

    # Convert input date to ordinal format for prediction (use current date or provided date)
    date_obj = pd.to_datetime(input_date)
    date_ordinal = date_obj.toordinal()
    future_dates = [[date_ordinal]]  # Reshaping into a 2D array (needed by model)
    predicted_attack = predictor.predict(future_dates)[0]

    # For attacker profile, we'll use the title to determine attacker's techniques (just an example logic)
    attacker_profile = profiler.predict([[2, 1]])[0]  # Example encoded input, update as needed

    # Return predictions
    return predicted_class, predicted_attack, attacker_profile

# Convert numpy types to native Python types for JSON serialization
def json_serial(obj):
    """Convert numpy int64 and other numpy types to native Python types."""
    if isinstance(obj, np.int64):  # Check for int64 type
        return int(obj)  # Convert to native int
    raise TypeError(f"Type {type(obj)} not serializable")

# Fetch all data from MongoDB
entries = fetch_all_data_from_mongo()

# Prepare the data to be written into the JSON file
results = []

if entries:
    for entry in entries:
        input_text = entry.get("description")
        title = entry.get("title")
        input_date = entry.get("date")
        url = entry.get("url", "No URL")  # Default to "No URL" if not available

        if input_text and title and input_date:
            # Call the prediction function with each entry's data
            predicted_class, predicted_attack, attacker_profile = make_predictions(input_text, title, input_date)

            # Store the results in a dictionary
            entry_result = {
                "url": url,
                "title": title,
                "description": input_text,
                "date": input_date,
                "predicted_class": predicted_class,
                "predicted_attack": predicted_attack,
                "attacker_profile": attacker_profile
            }

            # Add the result to the list
            results.append(entry_result)

            # Print Results for each entry
            print(f"URL: {url}")
            print(f"🛡️ Predicted Cyber Threat Category: {predicted_class}")
            print(f"📈 Predicted Future Attack Count (June 2025): {predicted_attack}")
            print(f"👤 Predicted Attacker Profile Target: {attacker_profile}")
            print("="*50)
        else:
            print(f"Missing data in entry: {entry}")

    # Write the results to 'legal_database.json'
    with open("database.json", "w") as f:
        json.dump(results, f, indent=4, default=json_serial)

else:
    print("No data found in MongoDB to make predictions.")
