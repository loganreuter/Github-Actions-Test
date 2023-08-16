import unittest
from src.main import add, sub

class TestCalculations(unittest.TestCase):
    def test_add(self):
        val = add(1,1)
        self.assertEqual(val, 2, "Should be 2")
    
    def test_sub(self):
        val = sub(1,1)
        self.assertEqual(val, 0, "Should be 0")
