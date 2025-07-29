import unittest
from ..my_sum import my_sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = my_sum.sum(data)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()