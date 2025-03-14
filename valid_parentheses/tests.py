from unittest import TestCase

from valid_parentheses.solution import is_valid

class TestIsValid(TestCase):
    def test_case_1(self):
        input_ = '()'
        self.assertTrue(is_valid(input_))

    def test_case_2(self):
        input_ = '()[]{}'
        self.assertTrue(is_valid(input_))

    def test_case_3(self):
        input_ = '(]'
        self.assertFalse(is_valid(input_))

    def test_case_4(self):
        input_ = '([])'
        self.assertTrue(is_valid(input_))

    def test_case_5(self):
        input_ = '([{'
        self.assertFalse(is_valid(input_))
