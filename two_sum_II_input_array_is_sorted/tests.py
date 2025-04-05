from unittest import TestCase

from two_sum_II_input_array_is_sorted.solution import two_sum


class TestSolution(TestCase):
    def test_case_1(self):
        inp = [2, 7, 11, 15]
        target = 9

        expected = [1, 2]
        real = two_sum(inp, target)
        self.assertListEqual(expected, real)

    def test_case_2(self):
        inp = [2, 3, 4]
        target = 6

        expected = [1, 3]
        real = two_sum(inp, target)
        self.assertListEqual(expected, real)

    def test_case_3(self):
        inp = [-1, 0]
        target = -1

        expected = [1, 2]
        real = two_sum(inp, target)
        self.assertListEqual(expected, real)
