def roman_to_int(s: str) -> int:
    digits = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1_000,
    }

    value = 0
    last_index = len(s) - 1
    index = 0
    while index < len(s):
        current_roman = s[index]
        current = digits[current_roman]

        next_roman = None
        next_ = None
        if index != last_index:
            next_roman = s[index + 1]
            next_ = digits[next_roman]

        if next_ and next_ > current:
            value += next_ - current
            index += 2
        else:
            value += current
            index += 1

    return value
