from unittest import TestCase
import json

from three_sum.solution import three_sum


class TestSolution(TestCase):
    def test_case_1(self):
        inp = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        real = three_sum(inp)
        self.assertListEqual(expected, real)

    def test_case_2(self):
        inp = [0, 1, 1]
        expected = []
        real = three_sum(inp)
        self.assertListEqual(expected, real)

    def test_case_3(self):
        inp = [0, 0, 0]
        expected = [[0, 0, 0]]
        real = three_sum(inp)
        self.assertListEqual(expected, real)

    def test_case_4(self):
        inp = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        real = three_sum(inp)
        self.assertListEqual(expected, real)

    def test_case_5(self):
        inp = [-1, 0, 1, 0]
        expected = [[-1, 0, 1]]
        real = three_sum(inp)
        self.assertListEqual(expected, real)

    def test_case_6(self):
        with open("three_sum/cases.json", "r") as cases:
            test_data = json.load(cases)
        inp = test_data["input"]
        expected = test_data["output"]
        real = three_sum(inp)
        self.assertListEqual(expected, real)
