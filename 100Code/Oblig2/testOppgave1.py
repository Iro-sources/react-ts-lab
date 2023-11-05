import unittest
from Oppgave1 import live_42

class TestLive42Function(unittest.TestCase):
    def test_live_42(self):
        result = live_42(42)
        self.assertEqual(result, "Det stemmer, meningen med livet er 42!")  # add assertion here

    def test_live_42_close_but_wrong(self):
        result = live_42(35)
        self.assertEqual(result, "Nærme, men feil")

    def test_live_42_wrong(self):
        result = live_42(20)
        self.assertEqual(result, "FEIL!")

if __name__ == '__main__':
    unittest.main()
