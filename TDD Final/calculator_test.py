import unittest
from calculator import Calculator
import math

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(math.pi/2), 1.0)

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(0), 1.0)

    def test_tan(self):
        self.assertAlmostEqual(self.calc.tan(math.pi/4), 1.0)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calc.sqrt(9), 3.0)

    def test_cbrt(self):
        self.assertAlmostEqual(self.calc.cbrt(27), 3.0)

if __name__ == '__main__':
    unittest.main()