import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.Add(1, 2), 3)
        self.assertEqual(self.calc.Add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.Subtract(5, 3), 2)
        self.assertEqual(self.calc.Subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.Multiply(2, 3), 6)
        self.assertEqual(self.calc.Multiply(-1, 5), -5)
        self.assertEqual(self.calc.Multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.Divide(6, 3), 2)
        with self.assertRaises(ValueError):
            self.calc.Divide(5, 0)

if __name__ == '__main__':
    unittest.main()
