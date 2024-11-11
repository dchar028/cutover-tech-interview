import requests
import base64
from .config import NASA_API_KEY, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def fetch_nasa_apod():
    nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(nasa_url)
    return response.json()

def get_spotify_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_data = {'grant_type': 'client_credentials'}
    auth_header = {
        'Authorization': 'Basic ' + base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    }
    response = requests.post(auth_url, headers=auth_header, data=auth_data)
    response.raise_for_status()
    return response.json()['access_token']

def fetch_spotify_top_track():
    access_token = get_spotify_access_token()
    playlist_url = "https://api.spotify.com/v1/playlists/37i9dQZEVXbLRQDuF5jeBp"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(playlist_url, headers=headers)
    data = response.json()
    top_track = data['tracks']['items'][0]['track']
    return {
        "name": top_track['name'],
        "artist": top_track['artists'][0]['name'],
        "album_image_url": top_track['album']['images'][0]['url']
    }
