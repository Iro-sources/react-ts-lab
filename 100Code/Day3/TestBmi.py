import unittest
from bmi2 import bmiCalculator
class TestBmiCalculator(unittest.TestCase):
    def test_under_weight(self):
        height = 1.70
        weight = 50.0
        result = bmiCalculator(height, weight)
        self.assertEqual(result, f"Your BMI is 17.30, You are underweight")

    def test_normal_weight(self):
        height = 1.75
        weight = 78
        result = bmiCalculator(height, weight)
        self.assertEqual(result, f"Your BMI is 24.49, You have a normal weight")

    def test_slightly_overweight(self):
        height = 1.75
        weight = 85
        result = bmiCalculator(height, weight)
        self.assertEqual(result, f"Your BMI is 27.76, You are slightly overweight")

    def test_obese(self):
        height = 1.75
        weight = 95
        result = bmiCalculator(height, weight)
        self.assertEqual(result, f"Your BMI is 31.02, You are obese")

    def test_clinically_obese(self):
        height = 1.75
        weight = 120
        result = bmiCalculator(height, weight)
        self.assertEqual(result, f"Your BMI is 39.18, You are clinically obese")