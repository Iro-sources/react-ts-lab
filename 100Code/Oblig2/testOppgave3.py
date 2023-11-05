import unittest
from Oppgave3Lister import book_list

class TestList(unittest.TestCase):
    def test_books(self):
        result = book_list()
        expected_books = ["The Hobbit", "Farmer", "Giles of Ham", "The Fellowship of the Ring",
                          "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]
        self.assertEqual(result, expected_books)


if __name__ == " __Main__ ":
    unittest.main()