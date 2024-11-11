from .fetch_data import fetch_nasa_apod, fetch_spotify_top_track
from .store_data import store_nasa_data, store_spotify_data

def main():
    # Fetch data
    nasa_data = fetch_nasa_apod()
    spotify_data = fetch_spotify_top_track()
    
    # Store data
    store_nasa_data(nasa_data)
    store_spotify_data(spotify_data)
    
    print("Data successfully fetched and stored in Redis.")

if __name__ == "__main__":
    main()
