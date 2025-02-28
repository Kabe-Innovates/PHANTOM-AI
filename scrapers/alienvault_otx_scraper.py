import requests
from datetime import datetime
from database.mongo_client import insert_data
import time

# Define your OTX API Key and Base URL
OTX_API_KEY = "acc1b57f952669c479198457ba7c49f47a567746ccb79d7ac3b76cb6c3a536e9"
OTX_BASE_URL = "https://otx.alienvault.com/api/v1/pulses/subscribed"

HEADERS = {
    "X-OTX-API-KEY": OTX_API_KEY,
    "Content-Type": "application/json"
}

def fetch_alienvault_threats():
    """Fetches latest cyber threat intelligence from AlienVault OTX."""
    response = requests.get(OTX_BASE_URL, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Failed to fetch AlienVault data, status code: {response.status_code}")
        return

    threat_data = response.json().get("results", [])
    structured_data = []

    # Process each threat entry from the fetched data
    for threat in threat_data:
        structured_entry = {
            "source": "https://otx.alienvault.com",
            "title": threat["name"],
            "url": f"https://otx.alienvault.com/pulse/{threat['id']}",
            "date": threat["created"],  # Ensure this is a valid datetime format if needed
            "description": threat["description"],
            "classification": "Unknown",  # Placeholder, can be updated later
            "attack_method": [],  # Can be extracted or updated based on available data
            "attack_vector": [],  # Same as above, to be updated if required
            "attacker_profile": {
                "group": threat.get("author_name", "Unknown"),
                "motivation": "Unknown",  # Placeholder
                "TTPs": []  # Placeholder, can be filled with relevant tactics, techniques, and procedures
            },
            "ioc": [indicator["indicator"] for indicator in threat.get("indicators", [])],  # Extract IOCs
            "target_industry": "Unknown",  # Placeholder for target industry
            "tech_stack_targeted": []  # Placeholder for tech stack
        }

        structured_data.append(structured_entry)

    # Insert structured data into MongoDB if available
    if structured_data:
        insert_data(structured_data)

def main():
    # Continuously fetch and update data every 3 minutes
    while True:
        print("Fetching the latest cyber threat data from AlienVault...")
        fetch_alienvault_threats()
        print("Data updated successfully.")
        time.sleep(180)  # Wait for 3 minutes before the next fetch

if __name__ == "__main__":
    main()
