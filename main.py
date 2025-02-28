import asyncio
import logging
from scrapers.alienvault_otx_scraper import fetch_alienvault_threats
# from scrapers.blog_scraper import scrape_blog  # If needed
from ai_model.predict import make_predictions, fetch_all_data_from_mongo  # From your predict.py
import json
from datetime import datetime
import pandas as pd
import json

# main.py
from reports.legal_report_generator import generate_and_send_reports


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

async def run_scraper(scraper_func, scraper_name, retries=3):
    """
    Runs a scraper function with retries.
    
    :param scraper_func: Scraper function to run.
    :param scraper_name: Name of the scraper for logging.
    :param retries: Number of times to retry on failure.
    """
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Starting {scraper_name} (Attempt {attempt}/{retries})")
            if asyncio.iscoroutinefunction(scraper_func):
                await scraper_func()
            else:
                await asyncio.to_thread(scraper_func)
            logging.info(f"{scraper_name} completed successfully.")
            return  # Exit if successful
        except Exception as e:
            logging.error(f"{scraper_name} failed on attempt {attempt}: {e}", exc_info=True)
            if attempt == retries:
                logging.critical(f"{scraper_name} failed after {retries} attempts. Moving on.")

async def scrape_data():
    """Scrape the necessary data."""
    await asyncio.gather(
        run_scraper(fetch_alienvault_threats, "AlienVault Scraper"),
        # run_scraper(scrape_blog, "Blog Scraper"),  # Enable if you want blog scraping
    )

def store_predictions_in_json(entries):
    """Store predictions in JSON after processing data."""
    results = []

    if entries:
        for entry in entries:
            input_text = entry.get("description")
            title = entry.get("title")
            input_date = entry.get("date")

            # Call the prediction function with each entry's data
            predicted_class, predicted_attack, attacker_profile = make_predictions(input_text, title, input_date)

            # Store the results in a dictionary
            entry_result = {
                "url": entry.get("url"),
                "title": entry.get("title"),
                "description": entry.get("description"),
                "date": entry.get("date"),
                "predicted_class": predicted_class,
                "predicted_attack": predicted_attack,
                "attacker_profile": attacker_profile
            }

            # Add the result to the list
            results.append(entry_result)

        # Write the results to 'legal_database.json'
        with open("legal_database.json", "w") as f:
            json.dump(results, f, indent=4)
        logging.info("Predictions stored in 'legal_database.json'.")
    else:
        logging.warning("No data found to make predictions.")



def convert_to_serializable(obj):
    """Recursively convert non-serializable types to serializable."""
    if isinstance(obj, pd.Series):
        return obj.tolist()  # Convert pandas Series to a list
    elif isinstance(obj, pd.DataFrame):
        return obj.to_dict(orient='records')  # Convert DataFrame to a list of dicts
    elif isinstance(obj, (int, float, str, bool, list, dict)):
        return obj  # Return primitive types as they are
    else:
        return str(obj)  # For any other types, return their string representation

def cognitive_deception(**attack):
    # Example data, can be replaced by your actual data
    log_entry = {
        "timestamp": "2025-03-01T12:34:56",
        "attacker_ip": "192.168.1.100",
        "attack_method": "SQL Injection",
        "severity": attack.get('severity', 4),
        "frequency": attack.get('frequency', 2),
        "tools_used": attack.get('tools_used', 3),
        "attacker_type": attack.get('attacker_type', "Script Kiddie"),
        "deception_applied": "Fake login error"
    }

    # Convert all elements to serializable formats
    log_entry_serializable = {k: convert_to_serializable(v) for k, v in log_entry.items()}

    # Now you can safely print the log_entry
    print(json.dumps(log_entry_serializable, indent=4))

# Example attack dictionary with int64 type
attack_data = {
    "severity": pd.Series([4], dtype='int64')[0],  # simulate an int64
    "frequency": 2,
    "tools_used": 3,
    "attacker_type": "Script Kiddie"
}

# Call the function
cognitive_deception(**attack_data)



def main():
    try:
        logging.info("Starting the cyber deception system.")
        
        # Step 1: Scrape data
        asyncio.run(scrape_data())
        
        # Step 2: Fetch all data from MongoDB
        entries = fetch_all_data_from_mongo()
        
        # Step 3: Make predictions and store them in a JSON file
        store_predictions_in_json(entries)
        
        logging.info("System completed successfully.")
    
    except KeyboardInterrupt:
        logging.info("Process interrupted. Exiting gracefully.")
    except Exception as e:
        logging.critical(f"Fatal error in main: {e}", exc_info=True)

if __name__ == "__main__":
    main()
    generate_and_send_reports()

