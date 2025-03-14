def is_valid(s: str) -> bool:
    stack = []
    parentheses = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in parentheses:
            stack.append(parentheses[char])
        else:
            if not stack or stack.pop() != char:
                return False

    if stack:
        return False

    return True
