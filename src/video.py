
import os
from googleapiclient.discovery import build

class Video:

    API_KEY: str = os.getenv('API_KEY')
    YOUTYBE = build('youtube', 'v3', developerKey=API_KEY)
    def __init__(self, video_id: str):

        video = Video.YOUTYBE.videos().list(part='snippet,statistics', id=video_id).execute()

        try:

            self.video_id = video_id
            self.title = video["items"][0]["snippet"]["title"]
            self.url = "https://youtube/" + video_id
            self.number_of_views = video["items"][0]["statistics"]["viewCount"]
            self.like_count = video["items"][0]["statistics"]["likeCount"]

        except IndexError:

            self.video_id = video_id
            self.title = None
            self.url = None
            self.number_of_views = None
            self.like_count = None

class PLVideo(Video):
    def __init__(self, video_id:str, playlist_id:str):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title


