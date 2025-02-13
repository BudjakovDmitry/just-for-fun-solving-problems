import unittest

from solution import solution

class TestSolution(unittest.TestCase):

    def test_min_string(self):
        real = solution("ht")
        expected = 12
        self.assertEqual(real, expected)

    def test_max(self):
        real = solution(
            "gqausliaurhtgkrcvaphdhzagzppubquqpkwhshhpswedwgqybxbbzpprcbrqyscorkmvzgdrzelxzssuigygbxaplkydfurbiiu"
        )
        expected = 996
        self.assertEqual(real, expected)

    def test_hello(self):
        real = solution("hello")
        expected = 13
        self.assertEqual(real, expected)

    def test_zaz(self):
        real = solution("zaz")
        expected = 50
        self.assertEqual(real, expected)


if __name__ == "__main__":
    unittest.main()
