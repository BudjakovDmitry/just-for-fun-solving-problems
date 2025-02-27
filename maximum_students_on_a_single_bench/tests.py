import unittest

from maximum_students_on_a_single_bench.solution import max_students


class TestSolution(unittest.TestCase):

    def test_zero(self):
        real = max_students([])
        expected = 0
        self.assertEqual(real, expected)

    def test_one(self):
        real = max_students([[1,2], [2,2], [3,3], [1,3], [2,3]])
        expected = 3
        self.assertEqual(real, expected)

    def test_two(self):
        real = max_students([[1,1], [2,1], [3,1], [4,2], [5,2]])
        expected = 3
        self.assertEqual(real, expected)

    def test_three(self):
        real = max_students([[1,1], [1,1]])
        expected = 1
        self.assertEqual(real, expected)

    def test_four(self):
        real = max_students([[1,1], [1,2], [2,1], [3,3], [1,1], [2,3], [4,3]])
        expected = 3
        self.assertEqual(real, expected)

    def test_five(self):
        real = max_students([[1,1], [1,2], [2,1], [2,2]])
        expected = 2
        self.assertEqual(real, expected)

if __name__ == '__main__':
    unittest.main()
