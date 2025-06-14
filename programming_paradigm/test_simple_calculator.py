import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, -9), -7)
        
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(12, 3), 9)
        
    def test_multiplication(self):
        """Test the multipliaction method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(12, -3), -36)
        self.assertEqual(self.calc.subtract(-7, -3), 21)
        
    def test_division(self):
        """Test the multipliaction method."""
        self.assertEqual(self.calc.division(12, 3), 4)
        self.assertEqual(self.calc.multiply(6, -3), 2)
        self.assertEqual(self.calc.subtract(10, 0), ZeroDivisionError)
        
if __name__ == "__main__":
    unittest.main()
        