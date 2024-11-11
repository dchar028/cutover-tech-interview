import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Check for required variables and warn if missing
required_vars = ["NASA_API_KEY", "SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET"]
for var in required_vars:
    if not globals()[var]:
        print(f"Warning: {var} is not set. Please update your .env file.")
