# Overview
This project fetches the NASA Astronomy Picture of the Day and the top Spotify track in the US, storing the data in Redis. It is designed to be self-contained, requiring minimal setup from new users, with only the .env file being unique to each user.

# Setup Instructions
## 1. Clone the repository:

```bash
git clone <repository_url>
cd project_folder
```

## 2. Install dependencies:
To ensure dependencies are installed in the correct Python environment, use:

```bash
pip install -r requirements.txt
```

This will install the required packages: `dotenv`, `requests`, `redis`, `python-dotenv`, and `PyQt5`.

## 3. Set up your environment variables:
Copy .env.template to .env:

```bash
cp .env.template .env
```
Open the .env file in a text editor and enter your API credentials:
> NASA_API_KEY: Your NASA API key.

> SPOTIFY_CLIENT_ID: Your Spotify Client ID.

> SPOTIFY_CLIENT_SECRET: Your Spotify Client Secret.

These credentials are required to access the NASA APOD API and Spotify API.

## 4. Run the application:
To launch the application and view today’s NASA image and top Spotify track:

```bash
python -m top_track_in_space.main
```
This will open the PyQt5 GUI, displaying today’s NASA APOD image, title, and description, as well as the Spotify top track, artist, and album cover.

# Usage

## GUI Features
- Daily NASA and Spotify Data: The GUI displays the NASA Astronomy Picture of the Day (APOD) and Spotify’s top track in the US for the current day.
- View All Entries: Click the "View All Entries" button to see a table of all stored data in Redis. Each row includes:
    - Date: The date for which data was stored.
    - Image URL: Link to the NASA image.
    - Track and Artist: Name of the Spotify top track and its artist.

## Data Storage in Redis
- Data Keys:
    - NASA APOD data is stored under keys in the format nasa:apod:YYYY-MM-DD.
    - Spotify track data is stored under keys in the format spotify:top_track:YYYY-MM-DD.
- Accessing Redis: Ensure that Redis is running locally on localhost:6379 for the application to store and retrieve data.

# Notes
- Redis: Ensure Redis is running on localhost:6379 for the application to connect and store data.
- Dependencies: All required dependencies are listed in requirements.txt and can be installed using pip.
- Configuration: API keys are loaded from .env to keep sensitive information secure.