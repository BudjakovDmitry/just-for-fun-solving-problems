from random import randint
from unittest import TestCase

from concatenation_of_array.solution import concatenation


class TestConcatenation(TestCase):
    def test_one_element(self):
        nums = [randint(1, 1_000)]
        expected = nums + nums
        real = concatenation(nums)
        self.assertListEqual(expected, real)

    def test_max_elements(self):
        nums = [randint(1, 1_000) for _ in range(1_000)]
        expected = nums + nums
        real = concatenation(nums)
        self.assertListEqual(expected, real)

    def test_middle_case_one(self):
        nums = [1, 2, 1]
        expected = [1, 2, 1, 1, 2, 1]
        real = concatenation(nums)
        self.assertListEqual(expected, real)

    def test_middle_case_two(self):
        nums = [1, 3, 2, 1]
        expected = [1, 3, 2, 1, 1, 3, 2, 1]
        real = concatenation(nums)
        self.assertListEqual(expected, real)
