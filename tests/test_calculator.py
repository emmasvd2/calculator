from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.mysum(1, 2), 3)

    def test_min(self):
        self.assertEqual(self.calculator.min(10, 2), 2)
        self.assertEqual(self.calculator.min(-1, -5), -5)

    def test_average(self):
        self.assertEqual(self.calc.myaverage(1, 2), 3)

if __name__ == '__main__':
    unittest.main()