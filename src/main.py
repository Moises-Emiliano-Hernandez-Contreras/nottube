from googleapiclient.discovery import build
import json
import correo
with open("config/config.json", "r") as config_file:
    config = json.load(config_file)

API_KEY=config["API_KEY"]
YOUTUBE_CHANNEL_ID = config["YOUTUBE_CHANNEL"]
youtube=build("youtube","v3",developerKey=API_KEY)
request = youtube.channels().list(
    part="snippet,statistics",
    id=YOUTUBE_CHANNEL_ID
)
response = request.execute()
print(response["items"][0]['snippet']["title"])
print(response["items"][0]['snippet']["description"])
print(correo.email)