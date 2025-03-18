from unittest import TestCase

from palindrome_number.solution import is_palindrome, is_palindrome_v2


class TestIsPalindromeV1(TestCase):
    def test_case_1(self):
        x = 121
        self.assertTrue(is_palindrome(x))

    def test_case_2(self):
        x = 156651
        self.assertTrue(is_palindrome(x))

    def test_case_3(self):
        x = -121
        self.assertFalse(is_palindrome(x))

    def test_case_4(self):
        x = 0
        self.assertTrue(is_palindrome(x))

    def test_case_5(self):
        x = 10
        self.assertFalse(is_palindrome(x))

    def test_case_6(self):
        x = 1234
        self.assertFalse(is_palindrome(x))


class TestIsPalindromeV2(TestCase):
    def test_case_1(self):
        x = 121
        self.assertTrue(is_palindrome_v2(x))

    def test_case_2(self):
        x = 156651
        self.assertTrue(is_palindrome_v2(x))

    def test_case_3(self):
        x = -121
        self.assertFalse(is_palindrome_v2(x))

    def test_case_4(self):
        x = 0
        self.assertTrue(is_palindrome_v2(x))

    def test_case_5(self):
        x = 10
        self.assertFalse(is_palindrome_v2(x))

    def test_case_6(self):
        x = 1234
        self.assertFalse(is_palindrome_v2(x))
