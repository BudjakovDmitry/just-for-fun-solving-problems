from unittest import TestCase

from two_sum.solution import two_sum


class TestTwoSum(TestCase):
    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertListEqual(two_sum(nums, target), [0, 1])

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertListEqual(two_sum(nums, target), [1, 2])

    def test_case_3(self):
        nums = [3, 3]
        target = 6
        self.assertListEqual(two_sum(nums, target), [0, 1])
