from unittest import TestCase

from divide_array_into_equal_pairs.solution import divide_array


class TestDivideArray(TestCase):
    def test_case_1(self):
        input_ = [1, 2, 3, 4]
        self.assertFalse(divide_array(input_))

    def test_case_2(self):
        input_ = [3, 2, 3, 2, 2, 2]
        self.assertTrue(divide_array(input_))

    def test_case_3(self):
        input_ = [1, 1, 1, 1, 1, 1]
        self.assertTrue(divide_array(input_))
