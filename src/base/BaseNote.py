from datetime import datetime

from src.base.Note import Note

#Базовий клас для нотаток основною відміннюстю є те, що він містить вже сам контент
class BaseNote(Note):
    def __init__(self, title, content, tags, importance):
        super().__init__(title, tags, importance)
        self.content = content

    def update(self, title=None, content=None, tags=None, importance=None):
        super().update(title, tags, importance)
        if content:
            self.content = content
        self.updated_at = datetime.now()