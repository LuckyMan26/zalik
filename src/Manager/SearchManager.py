from src.Manager.BaseManager import BaseManager

#Цей клас відповідає за пошук нотатків за заданими умовами
class SearchManager:
    @staticmethod
    def search_by_content( notes, keyword):
        return [note for note in notes if keyword in note.content]

    @staticmethod
    def search_by_time_range(notes, start_time, end_time):
        return [note for note in notes if start_time <= note.created_at <= end_time]

    @staticmethod
    def search_by_tags(notes, tags):
        return [note for note in notes if any(tag in note.tags for tag in tags)]
