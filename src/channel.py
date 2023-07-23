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

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel_id = 'AIzaSyAaLeB15LutRrAZvoCVnnB5cvg2YDvpJM0'
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)
