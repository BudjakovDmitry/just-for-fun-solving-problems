from unittest import TestCase

from valid_palindrome.solution import is_palindrome


class TestSolution(TestCase):
    def test_case_1(self):
        inp = "A man, a plan, a canal: Panama"
        self.assertTrue(is_palindrome(inp))

    def test_case_2(self):
        inp = "race a car"
        self.assertFalse(is_palindrome(inp))

    def test_case_3(self):
        inp = " "
        self.assertTrue(is_palindrome(inp))

    def test_case_4(self):
        inp = "Go 4 deliver a dare vile d4og"
        self.assertTrue(is_palindrome(inp))
