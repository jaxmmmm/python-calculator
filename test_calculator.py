import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
    def test_add2(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 5), 1)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(4, 10), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(5, 9), 45)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(12, 4), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10, 4), 2)
    
if __name__ == '__main__':
    unittest.main()