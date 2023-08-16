import unittest
from src.main import add

class TestCalculations(unittest.TestCase):
    def test_add_a(self):
        val = add(1,1)
        self.assertEqual(val, 2, "Should be 2")
    
    def test_add_b(self):
        val = add(1,1)
        self.assertEqual(val, 1, "Should be 1")
