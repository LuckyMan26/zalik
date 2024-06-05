#Цей клас відповідає за сортування нотатків за певними критеріями
class SortManager:
    @staticmethod
    def sort_by_last_change(notes):
        return sorted(notes, key=lambda note: note.updated_at, reverse=True)

    @staticmethod
    def sort_by_importance(notes):
        return sorted(notes, key=lambda note: note.importance, reverse=True)

    @staticmethod
    def sort_by_title(notes):
        return sorted(notes, key=lambda note: note.title)