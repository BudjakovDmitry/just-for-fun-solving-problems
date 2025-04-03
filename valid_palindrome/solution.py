def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        left_letter = s[left]
        if not left_letter.isalnum():
            left += 1
            continue

        right_letter = s[right]
        if not right_letter.isalnum():
            right -= 1
            continue

        if left_letter.lower() != right_letter.lower():
            return False
        left += 1
        right -= 1

    return True