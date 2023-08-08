import os
import datetime
import isodate
from googleapiclient.discovery import build
from src.video import Video

class PlayList:
    """Получаем информацию о плейлисте"""

    API_KEY: str = os.getenv('API_KEY')
    YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, playlist_id: str) -> None:

        self.playlist_info = PlayList.YOUTUBE.playlists().list(id=playlist_id,
                                                               part='snippet,contentDetails',
                                                               maxResults=50).execute()

        self.playlist = PlayList.YOUTUBE.playlistItems().list(playlistId=playlist_id,
                                                              part='snippet,contentDetails,id,status',
                                                              maxResults=50).execute()

        #id всех видеороликов
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist['items']]

        #длительность всех видеороликов
        video_response = PlayList.YOUTUBE.videos().list(part='contentDetails,statistics',
                                                        id=','.join(video_ids)).execute()

        #общая длительность видеороликов
        delta = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            delta += duration

        self.title = self.playlist_info["items"][0]["snippet"]["title"]
        self.url = "https://www.youtube.com/playlist?list=" + playlist_id
        self.__total_duration = delta

    @property
    def total_duration(self):
        return self.__total_duration

    def show_best_video(self):
        #id всех видеороликов
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist['items']]

        #Находим самое популярное видео
        max_count_of_likes = 0
        for row in video_ids:
            video = Video(row)
            if int(video.like_count) > max_count_of_likes:
                best_video = video
        return best_video.url