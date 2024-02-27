import unittest
from green_version import Calculator

class CalculatorTest(unittest.TestCase):

    def test_addition(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiplication(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_division(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
