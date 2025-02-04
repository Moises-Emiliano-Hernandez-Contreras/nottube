from googleapiclient.discovery import build
import json
# Cargar configuración desde config.json
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
"""for item in response['items']:
    print("Nombre del canal:", item['snippet']['title'])
    print("Descripción:", item['snippet']['description'])"""

"""print(response)"""
print(response["items"][0]['snippet']["title"])
print(response["items"][0]['snippet']["description"])