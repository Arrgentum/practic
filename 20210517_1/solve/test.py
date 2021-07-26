import unittest
from solve import solve

class TestMo(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(solve(2.0, 5.0), -2.5)
        self.assertEqual(solve(5.6, 7.0), -1.25)
        self.assertEqual(solve(-8.9, 0.0), 0.0)
        self.assertEqual(solve(-100.0, 9.0), 0.09)
        self.assertEqual(solve(-0.1, -80.0), -800.0)

    def test_2(self):
        self.assertEqual(solve(0.0, 5.0), None)
        self.assertEqual(solve(0.0, -90.1), None)
        self.assertEqual(solve(-0.0, 45.4), None)
        self.assertEqual(solve(-0.0, -89.0), None)
        self.assertEqual(solve(0.0, 0.1), None)



