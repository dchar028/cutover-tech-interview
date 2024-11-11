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

def get_all_data():
    data = []
    for key in r.keys("nasa:apod:*"):
        date_key = key.decode().split(":")[-1]
        nasa_data = eval(r.get(key).decode())
        spotify_key = f"spotify:top_track:{date_key}"
        spotify_data = r.get(spotify_key)
        if spotify_data:
            spotify_data = eval(spotify_data.decode())
            data.append({
                "date": date_key,
                "image_url": nasa_data.get("url"),
                "track_name": spotify_data.get("name"),
                "artist": spotify_data.get("artist")
            })
    return data
