from src.base.BaseNote import BaseNote


class TextNote(BaseNote):
    def __init__(self, title, content, tags, importance):
        super().__init__(title, content, tags, importance)