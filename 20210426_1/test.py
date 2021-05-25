import unittest
from task import func

class TestTdfun(unittest.TestCase):
    def test_1_func(self):
        self.assertEqual(func(1, 4, 4), (-2, -2))
    def test_2_func(self):
        self.assertEqual(func(1, -1, 4), None)
    def test_3_func(self):
        self.assertEqual(func(1, -3, 2), (1, 2))
	



