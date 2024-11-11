import requests
from .config import NASA_API_KEY, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
import base64

def fetch_nasa_apod():
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}")
    response.raise_for_status()
    return response.json()

def fetch_spotify_top_track():
    auth_header = {
        'Authorization': 'Basic ' + base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    }
    token_response = requests.post('https://accounts.spotify.com/api/token', headers=auth_header, data={'grant_type': 'client_credentials'})
    token_response.raise_for_status()
    access_token = token_response.json()['access_token']

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://api.spotify.com/v1/playlists/37i9dQZEVXbLRQDuF5jeBp", headers=headers)
    response.raise_for_status()
    top_track = response.json()['tracks']['items'][0]['track']
    return {
        "name": top_track['name'],
        "artist": top_track['artists'][0]['name'],
        "album_image_url": top_track['album']['images'][0]['url']
    }
