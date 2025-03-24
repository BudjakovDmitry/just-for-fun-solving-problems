from unittest import TestCase

from longest_common_prefix.solution import longest_common_prefix

class TestSolution(TestCase):
    def test_case_1(self):
        inp = ["flower", "flow", "flight"]
        self.assertEqual(longest_common_prefix(inp), "fl")

    def test_case_2(self):
        inp = ["dog", "racecar", "car"]
        self.assertEqual(longest_common_prefix(inp), "")
