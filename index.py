from googleapiclient.discovery import build
API_KEY="AIzaSyBSv7VTQhkvJr-dX4f2PktWCNn2Ji3_kJc"
YOUTUBE_CHANNEL_ID = "UCG7pu4yj5lvVScl3HJZIYPw"
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