from datetime import datetime

#Базовий клас для всіх нотаток
class Note:
    def __init__(self, title, tags, importance):
        self.title = title
        self.tags = tags
        self.importance = importance
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, title=None, tags=None, importance=None):
        if title:
            self.title = title
        if tags:
            self.tags = tags
        if importance:
            self.importance = importance
        self.updated_at = datetime.now()
