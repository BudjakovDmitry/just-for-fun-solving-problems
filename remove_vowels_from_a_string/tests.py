import random
import string
import unittest

from .solution import remove_vowels


class TestRemoveVowels(unittest.TestCase):
    def test_normal_input(self):
        result = remove_vowels('leetcodeisacommunityforcoders')
        self.assertEqual(result, 'ltcdscmmntyfrcdrs')

    def test_one_symbol_not_removable(self):
        symbol = 't'
        result = remove_vowels(symbol)
        self.assertEqual(result, symbol)

    def test_all_symbols_removable(self):
        result = remove_vowels('aeiou')
        self.assertEqual(result, '')

    def test_one_removable_symbol(self):
        result = remove_vowels('a')
        self.assertEqual(result, '')

    def test_max_length(self):
        input_string = "".join(
            random.choice(string.ascii_lowercase) for _ in range(1_000)
        )
        expected = (
            input_string.replace('a', '')
            .replace('e', '')
            .replace('i', '')
            .replace('o', '')
            .replace('u', '')
        )

        real = remove_vowels(input_string)
        self.assertEqual(expected, real)
