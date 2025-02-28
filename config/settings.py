# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()



# MONGO_URI: "mongodb+srv://jaiyantan:js123@cluster0.5tbd1.mongodb.net/",
#     "DB_NAME":  "cyber_threat_db",
#     "THREAT_COLLECTION":  "threat_intelligence"


# ALIENVAULT_API_URL = "https://otx.alienvault.com/api/v1/pulses/subscribed"
# ALIENVAULT_API_KEY = "acc1b57f952669c479198457ba7c49f47a567746ccb79d7ac3b76cb6c3a536e9"

import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if available)
load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://jaiyantan:js123@cluster0.5tbd1.mongodb.net/")

# AlienVault OTX API Key
OTX_API_KEY = os.getenv("OTX_API_KEY", "acc1b57f952669c479198457ba7c49f47a567746ccb79d7ac3b76cb6c3a536e9")

# Playwright Settings
PLAYWRIGHT_TIMEOUT = 60000  # Timeout in milliseconds (60 seconds)
HEADLESS_MODE = True  # Set to False to see browser actions during scraping

# Cybersecurity Blog Sources
BLOG_SOURCES = [
    "https://www.cm-alliance.com/cybersecurity-blog",
    "https://www.ibm.com/blog/category/cybersecurity/",
    "https://cyberhoot.com/category/blog/",
    "https://www.sans.org/blog/",
    "https://www.tarlogic.com/blog/category/cybersecurity/",
    "https://www.infosecurity-magazine.com/blogs/",
]

# Threat Classification Keywords
THREAT_CATEGORIES = {
    "malware": ["malware", "ransomware", "trojan", "worm", "stealer"],
    "phishing": ["phishing", "social engineering", "spoofing"],
    "APT": ["nation-state", "APT", "cyber espionage", "hacker group"],
    "DDoS": ["denial of service", "DDoS", "botnet"],
    "exploits": ["zero-day", "exploit", "vulnerability"],
}

# Logging Settings
LOGGING_ENABLED = True
LOG_FILE = "scraper.log"

# config.py
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USER = 'jaiyantanjaiyantan34509@gmail.com'  # Use your Gmail address here
EMAIL_PASSWORD = 'cmnt uptm ujlf fxnd'  # Use your email password or app-specific password

