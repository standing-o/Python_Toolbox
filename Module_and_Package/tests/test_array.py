import unittest
from algorithms import array

class TestArray(unittest.TestCase):
    # Create class instance
    def setUp(self):
        self.array = array.Array('1 2 3 4 10 11')
