from src.channel import youtube
import isodate

class Video:
    def __init__(self, video_id: str) -> None:

        self.video_id = video_id

        video_id = 'AWX4JnAnjBE'
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()

        self.video_title = video_response['items'][0]['snippet']['title']
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']


class PLVideo:
    def __init__(self, video_id, playlist_id):
        self.video_id = video_id
        video_id = '4fObz_qw9u4'
        self.playlist_id = playlist_id
        playlists = youtube.playlists().list(id=video_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        for playlist in playlists['items']:
            print(playlist)
            print()

        playlist_id = 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
        playlist_videos = youtube.playlists().list(part="snippet", id=playlist_id, maxResults=50).execute()
        video_ids = [video['id'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            print(duration)

    def __str__(self):
        return f'{self.video_id}, {self.playlist_id}'


