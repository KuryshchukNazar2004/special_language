import unittest
from classes.calculator import Calculator
import os

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        open("History.txt", "w").close()

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

    def test_mod(self):
        self.assertEqual(self.calc.Mod(10, 3), 1)
        self.assertEqual(self.calc.Mod(10, 5), 0)

    def test_square_root(self):
        self.assertEqual(self.calc.SquareRoot(4), 2)
        self.assertEqual(self.calc.SquareRoot(9), 3)

    def test_exponentiate(self):
        self.assertEqual(self.calc.Exponentiate(2, 3), 8)
        self.assertEqual(self.calc.Exponentiate(5, 0), 1)

    def test_get_history(self):
        self.calc.Add(1, 1)
        self.calc.Subtract(5, 2)
        history = self.calc.GetHistory()
        self.assertIn("1 + 1 = 2", history)
        self.assertIn("5 - 2 = 3", history)

    def tearDown(self):
        if os.path.exists("History.txt"):
            os.remove("History.txt")

if __name__ == '__main__':
    unittest.main()
