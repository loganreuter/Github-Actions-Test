import unittest
from src.main import add, sub, mul

class TestCalculations(unittest.TestCase):
    def test_add(self):
        val = add(1,1)
        self.assertEqual(val, 2, "Should be 2")
    
    def test_sub(self):
        val = sub(1,1)
        self.assertEqual(val, 0, "Should be 0")
    
    def test_mul(self):
        val = mul(2,2)
        self.assertEqual(val, 3, "Should be 3")
