from unittest import TestCase

from maximum_count_of_positive_integer_and_negative_integer.solution import (
    maximum_count
)


class TestSolution(TestCase):
    def test_case_1(self):
        nums = [-2, -1, -1, 1, 2, 3]
        self.assertEqual(maximum_count(nums), 3)

    def test_case_2(self):
        nums = [-3, -2, -1, 0, 0, 1, 2]
        self.assertEqual(maximum_count(nums), 3)

    def test_case_3(self):
        nums = [5, 20, 66, 1314]
        self.assertEqual(maximum_count(nums), 4)

    def test_case_4(self):
        nums = [0] * 100
        self.assertEqual(maximum_count(nums), 0)

    def test_case_5(self):
        nums = [-151, -54, -23, -14, -5, -2, -1]
        self.assertEqual(maximum_count(nums), 7)
