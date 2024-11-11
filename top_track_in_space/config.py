from dotenv import load_dotenv
import os

# Load and retrieve environment variables
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
