import redis
from datetime import datetime

# Initialize Redis connection
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def store_nasa_data(nasa_data):
    date_key = datetime.now().strftime("%Y-%m-%d")
    r.set(f"nasa:apod:{date_key}", str(nasa_data))

def store_spotify_data(spotify_data):
    date_key = datetime.now().strftime("%Y-%m-%d")
    r.set(f"spotify:top_track:{date_key}", str(spotify_data))

def get_data(key):
    return r.get(key)
