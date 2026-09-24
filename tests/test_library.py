import unittest

from modules.data import books, members
from modules.books import add_book
from modules.members import add_member


class TestLibrary(unittest.TestCase):

    def setUp(self):
        books.clear()
        members.clear()

    def test_add_book(self):
        books.append({
            "id": "B1",
            "title": "Python",
            "author": "John",
            "available": True
        })

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Python")

    def test_add_member(self):
        members.append({
            "id": "M1",
            "name": "Dhara"
        })

        self.assertEqual(len(members), 1)
        self.assertEqual(members[0]["name"], "Dhara")


if __name__ == "__main__":
    unittest.main()