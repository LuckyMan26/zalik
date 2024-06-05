#Базовий менеджер,який відповідає за CRUD операції
class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, note):
        self.notes.append(note)

    def read_note(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None

    def update_note(self, title, **kwargs):
        note = self.read_note(title)
        if note:
            note.update(**kwargs)
            return note
        return None

    def delete_note(self, title):
        note = self.read_note(title)
        if note:
            self.notes.remove(note)
            return True
        return False

    def list_notes(self):
        return self.notes