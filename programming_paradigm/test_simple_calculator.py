import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # Addition tests
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-4, -7), -11)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(1e6, 1e6), 2e6)

    # Subtraction tests
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-3, -6), 3)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(8, 8), 0)

    # Multiplication tests
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, -5), 10)
        self.assertEqual(self.calc.multiply(6, -3), -18)
        self.assertEqual(self.calc.multiply(9, 0), 0)
        self.assertEqual(self.calc.multiply(1e3, 1e3), 1e6)

    # Division tests
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-8, -2), 4)
        self.assertEqual(self.calc.divide(9, -3), -3)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertEqual(self.calc.divide(0, 7), 0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main()
