import requests
import os

API_KEY = os.getenv('YOUTUBE_API_KEY')
url = "https://www.googleapis.com/youtube/v3/videos"
params = {
    "part": "snippet",
    "chart": "mostPopular",
    "regionCode": "US",
    "maxResults": 5,
    "key": API_KEY,
}

response = requests.get(url, params=params)
print(response.json())
