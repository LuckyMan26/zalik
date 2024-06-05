import unittest
from datetime import datetime

from src.ImageNote import ImageNote
from src.ListNote import ListNote
from src.Manager.SearchManager import SearchManager
from src.Manager.SortManager import SortManager
from src.Manager.NoteManager import NoteManager
from src.TextNote import TextNote


class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.manager = NoteManager()
        self.text_note = TextNote(
            title="Text Note 1",
            content="This is a text note.",
            tags=["personal", "urgent"],
            importance=5
        )
        self.image_note = ImageNote(
            title="Image Note 1",
            image_path="path/to/image.jpg",
            tags=["work"],
            importance=3
        )
        self.list_note = ListNote(
            title="List Note 1",
            items=["Item one", "Item two"],
            tags=["shopping"],
            importance=4
        )
        self.manager.create_note(self.text_note)
        self.manager.create_note(self.image_note)
        self.manager.create_note(self.list_note)

    def test_create_and_read_note(self):
        self.assertEqual(self.manager.read_note("Text Note 1"), self.text_note)

    def test_update_note(self):
        self.manager.update_note("Text Note 1", content="Updated content.")
        self.assertEqual(self.text_note.content, "Updated content.")

    def test_delete_note(self):
        self.manager.delete_note("Image Note 1")
        self.assertIsNone(self.manager.read_note("Image Note 1"))

    def test_search_by_content(self):
        results = SearchManager.search_by_content(self.manager.list_notes(), "text note")
        self.assertIn(self.text_note, results)

    def test_search_by_time_range(self):
        start_time = datetime.now()
        end_time = datetime.now()
        results = SearchManager.search_by_time_range(self.manager.list_notes(), start_time, end_time)
        self.assertGreaterEqual(len(results), 1)

    def test_search_by_tags(self):
        results = SearchManager.search_by_tags(self.manager.list_notes(), ["personal"])
        self.assertIn(self.text_note, results)

    def test_sort_by_last_change(self):
        results = SortManager.sort_by_last_change(self.manager.list_notes())

        self.assertEqual(results[0], self.text_note)

    def test_sort_by_importance(self):
        results = SortManager.sort_by_importance(self.manager.list_notes())
        self.assertEqual(results[0], self.text_note)

    def test_sort_by_title(self):
        results = SortManager.sort_by_title(self.manager.list_notes())
        self.assertEqual(results[0], self.image_note)

    def test_change_image(self):
        self.image_note.change_image("new/path/to/image.jpg")
        self.assertEqual(self.image_note.image_path, "new/path/to/image.jpg")

    def test_add_list_item(self):
        self.list_note.add_item("Item three")
        self.assertIn("Item three", self.list_note.items)
        self.assertIn("Item three", self.list_note.content)

    def test_remove_list_item(self):
        self.list_note.remove_item("Item two")
        self.assertNotIn("Item two", self.list_note.items)
        self.assertNotIn("Item two", self.list_note.content)

if __name__ == '__main__':
    unittest.main()
