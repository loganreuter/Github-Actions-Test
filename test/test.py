import unittest

from src.main import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,2), 4)
    
    def test_sub(self):
        self.assertEqual(sub(2,2), 0)
    
    def test_mul(self):
        self.assertEqual(mul(2,2), 4)
    
    def test_div(self):
        self.assertEqual(div(2,2), 1)