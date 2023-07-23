import json
import os
from googleapiclient.discovery import build

value = os.getenv('API_KEY')
#print(value)

# создаем специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=value)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id

        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet, statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.channel_descr = channel['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/" + channel['items'][0]['snippet']['customUrl']
        self.quantity_sub = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.quantity_all_views = channel['items'][0]['statistics']['videoCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel_id = 'AIzaSyAaLeB15LutRrAZvoCVnnB5cvg2YDvpJM0'
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""

        return build('youtube', 'v3', developerKey='AIzaSyAaLeB15LutRrAZvoCVnnB5cvg2YDvpJM0')

    def to_json(self, file_name):
        with open(file_name, 'wt') as file:
            text = {'channel_id': self.channel_id, 'title': self.title,
                    'channel_descr': self.channel_descr, 'url': self.url,
                    'quantity_sub': self.quantity_sub, 'video_count': self.video_count,
                    'quantity_all_views': self.quantity_all_views}
            json_text = json.dumps(text, ensure_ascii=False, indent=2)
            file.write(json_text)


