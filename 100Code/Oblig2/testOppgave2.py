import unittest
from Oppgave2Løkker import odds
from io import StringIO
import sys

class TestOddsGenerator(unittest.TestCase):
    def test_odd_values_9_to_101(self):
        expected_values = [i for i in range(9, 102) if i % 2 != 0]
        generated_values = list(odds(9, 102))
        self.assertEqual(generated_values, expected_values)


if __name__ == "__main__":
    unittest.main()


