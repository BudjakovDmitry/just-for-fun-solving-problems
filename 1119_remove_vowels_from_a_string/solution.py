def remove_vowels(s: str) -> str:
    return ''.join(letter for letter in s if letter not in {'a', 'e', 'i', 'o', 'u'})
