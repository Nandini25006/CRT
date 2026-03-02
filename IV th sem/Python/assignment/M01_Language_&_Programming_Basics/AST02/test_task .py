import unittest
from task.py import even_odd

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(even_odd(5), "Weird")

    def test_multiple_digits(self):
        self.assertEqual(even_odd(25), "Not Weird")

    def test_with_zero(self):
        self.assertEqual(even_odd(70), "Not Weird")

if __name__ == "__main__":
    unittest.main()
