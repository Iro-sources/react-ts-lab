import unittest

from numberChecker import number_checker

class TestNumberChecker(unittest.TestCase):
    def test_odd_number(self):
        result = number_checker(8)
        self.assertEqual(result, "odd")


    def test_even_number(self):
        result = number_checker(7)
        self.assertEqual(result, "even")


if __name__ == '__main__':
        unittest.main()


