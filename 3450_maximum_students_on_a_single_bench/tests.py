import unittest

from solution import solution


class TestStringMethods(unittest.TestCase):

    def test_zero(self):
        real = solution([])
        expected = 0
        self.assertEqual(real, expected)

    def test_one(self):
        real = solution([[1,2], [2,2], [3,3], [1,3], [2,3]])
        expected = 3
        self.assertEqual(real, expected)

    def test_two(self):
        real = solution([[1,1], [2,1], [3,1], [4,2], [5,2]])
        expected = 3
        self.assertEqual(real, expected)

    def test_three(self):
        real = solution([[1,1], [1,1]])
        expected = 1
        self.assertEqual(real, expected)

    def test_four(self):
        real = solution([[1,1], [1,2], [2,1], [3,3], [1,1], [2,3], [4,3]])
        expected = 3
        self.assertEqual(real, expected)

    def test_five(self):
        real = solution([[1,1], [1,2], [2,1], [2,2]])
        expected = 2
        self.assertEqual(real, expected)

if __name__ == '__main__':
    unittest.main()
