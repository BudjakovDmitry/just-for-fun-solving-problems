from unittest import TestCase

from roman_to_integer.solution import roman_to_int


class TestSolution(TestCase):
    def test_case_1(self):
        inp = "III"
        self.assertEqual(roman_to_int(inp), 3)

    def test_case_2(self):
        inp = "LVIII"
        self.assertEqual(roman_to_int(inp), 58)

    def test_case_3(self):
        inp = "MCMXCIV"
        self.assertEqual(roman_to_int(inp), 1994)

    def test_case_4(self):
        inp = "MCDLXXVI"
        self.assertEqual(roman_to_int(inp), 1476)
