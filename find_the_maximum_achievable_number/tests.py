from unittest import TestCase

from find_the_maximum_achievable_number.solution import max_achievable_x


class TestMaxAchievableNumber(TestCase):
    def test_case_one(self):
        num = 4
        t = 1
        result = max_achievable_x(num, t)
        self.assertEqual(result, 6)

    def test_case_two(self):
        num = 3
        t = 2
        result = max_achievable_x(num, t)
        self.assertEqual(result, 7)
