def is_palindrome(x: int) -> bool:
    """Solution with converting integer to a string"""
    if x < 0:
        return False
    x = str(x)
    return x == x[::-1]


def is_palindrome_v2(x: int) -> bool:
    """Solution without converting integer to a string"""
    if x < 0:
        return False

    digits = []
    while x:
        digits.append(x % 10)
        x = x // 10

    for i, d in enumerate(digits):
        j = len(digits) - 1 - i
        if d != digits[j]:
            return False

    return True
