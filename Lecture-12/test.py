import unittest
from add_file import add
# pylint: disable=C0114
#disable missing doc string
class TestAdd(unittest.TestCase):

    def test_positive_numbers(self):

        self.assertEqual(add(2, 3), 5)
    
    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
