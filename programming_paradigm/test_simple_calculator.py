import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # Addition tests
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-4, -7), -11)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_add_large_numbers(self):
        self.assertEqual(self.calc.add(1e6, 1e6), 2e6)

    # Subtraction tests
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -6), 3)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_subtract_resulting_in_zero(self):
        self.assertEqual(self.calc.subtract(8, 8), 0)

    # Multiplication tests
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(6, -3), -18)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(9, 0), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(self.calc.multiply(1e3, 1e3), 1e6)

    # Division tests
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-8, -2), 4)

    def test_divide_positive_and_negative(self):
        self.assertEqual(self.calc.divide(9, -3), -3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 7), 0)

    def test_divide_float_result(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

if __name__ == "__main__":
    unittest.main()
