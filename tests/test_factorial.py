import unittest
from mymath.factorial import factorial
"""
RUN from main directory:
    python -m unittest tests/test_factorial.py
    python -m unittest -v tests/test_factorial.py
"""

#  Unit test class -> must make sure the right logic (or answer) is provided, as the 
# test will fail incorrectly otherwise -> both the code & test code must be correct
class TestFactorialFunctions(unittest.TestCase):

    def test_3(self):
        self.assertEqual(factorial(3), 6)

    def test_5(self):
        self.assertEqual(factorial(5), 120)

#  test for exceptions
    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)