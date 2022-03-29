import googleapiclient.discovery
import pandas as pd

channel_id = ""

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyAFcHNZ8qndQN4oCDJ4xtmjJZM3qNNivIU")

request = youtube.playlists().list(
    part = "snippet",
    channelId = channel_id,
    maxResults = 50
)
response = request.execute()

playlists = []
while request is not None:
    response = request.execute()
    playlists += response["items"]
    request = youtube.playlists().list_next(request, response)

print(f"total: {len(playlists)}")
print(playlists)

pd.DataFrame(playlists)