# Overview
This project fetches the NASA Astronomy Picture of the Day and the top Spotify track in the US, storing the data in Redis. It is designed to be self-contained, requiring minimal setup from new users, with only the .env file being unique to each user.

# Setup Instructions
## 1. Clone the repository:

```bash
git clone <repository_url>
cd project_folder
```

## 2. Install dependencies:

```bash
pip install -r requirements.txt
```
## 3. Set up your environment variables:
Copy .env.template to .env:

```bash
cp .env.template .env
```
Open the .env file in a text editor and enter your API credentials:
> NASA_API_KEY: Your NASA API key.

> SPOTIFY_CLIENT_ID: Your Spotify Client ID.

> SPOTIFY_CLIENT_SECRET: Your Spotify Client Secret.

## 4. Run the application:
To fetch the data and store it in Redis, use:

```bash

python -m project_name.main
```

# Usage
Data fetched: The NASA Astronomy Picture of the Day (APOD) and the current top track on Spotify in the US.
Storage: Data is stored in Redis under unique keys for each day, allowing easy retrieval.

# Notes
Ensure Redis is running on localhost:6379 for the application to connect and store data.
For customized Redis configurations, modify the `store_data.py` file in the `top track in space` package as needed.
