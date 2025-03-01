from unittest import TestCase

from apply_operations_to_an_array.solution import Solution


class TestApplyOperations(TestCase):
    def test_many(self):
        input_ = [1, 2, 2, 1, 1, 0]
        expected = [1, 4, 2, 0, 0, 0]
        real = Solution.apply_operations(input_)
        self.assertListEqual(expected, real)

    def test_two(self):
        input_ = [0, 1]
        expected = [1, 0]
        real = Solution.apply_operations(input_)
        self.assertListEqual(expected, real)


class TestShiftZeros(TestCase):
    def test_shift_two(self):
        input_ = [1, 0]
        expected = [1, 0]
        real = Solution.shift_zeros(input_)
        self.assertListEqual(expected, real)

    def test_shift_two_mix(self):
        input_ = [0, 1]
        expected = [1, 0]
        real = Solution.shift_zeros(input_)
        self.assertListEqual(expected, real)

    def test_without_zeros(self):
        input_ = [1, 4, 1, 6, 15, 2, 7, 4]
        expected = [1, 4, 1, 6, 15, 2, 7, 4]
        real = Solution.shift_zeros(input_)
        self.assertListEqual(expected, real)

    def test_multiply_zeros(self):
        input_ = [1, 0, 4, 4, 2, 0, 3, 2, 0]
        expected = [1, 4, 4, 2, 3, 2, 0, 0, 0]
        real = Solution.shift_zeros(input_)
        self.assertListEqual(expected, real)

    def test_zeros_only(self):
        input_ = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        real = Solution.shift_zeros(input_)
        self.assertListEqual(expected, real)
