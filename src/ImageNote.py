from datetime import datetime

from src.base.BaseNote import BaseNote

#Нотатка з зображенням
class ImageNote(BaseNote):
    def __init__(self, title, image_path, tags, importance,text=None):
        content = f"Text: {text}, Image Path: {image_path}"
        super().__init__(title, content, tags, importance)
        self.image_path = image_path

    def change_image(self, new_image_path=None, title=None, text=None, tags=None, importance=None):
        if new_image_path:
            self.image_path = new_image_path
        content = f"Text: {text}, Image Path: {new_image_path}"
        self.update(title, content, tags, importance)
