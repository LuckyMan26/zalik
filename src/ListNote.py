from datetime import datetime

from src.base.BaseNote import BaseNote


class ListNote(BaseNote):
    def __init__(self, title, items, tags, importance):
        content = '\n'.join(items)
        super().__init__(title, content, tags, importance)
        self.items = items

    def add_item(self, item):
        self.items.append(item)

        content = '\n'.join(self.items)
        self.update(content=content)


    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            content = '\n'.join(self.items)
            self.update(content=content)