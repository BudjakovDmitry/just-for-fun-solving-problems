from unittest import TestCase

from reverse_string.solution import reverse_string


class TestReverseString(TestCase):
    def test_case_1(self):
        s = ["h", "e", "l", "l", "o"]
        reverse_string(s)
        self.assertListEqual(s, ["o", "l", "l", "e", "h"])

    def test_case_2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        reverse_string(s)
        self.assertListEqual(s, ["h", "a", "n", "n", "a", "H"])

    def test_case_3(self):
        s = ["A"]
        reverse_string(s)
        self.assertListEqual(s, ["A"])
