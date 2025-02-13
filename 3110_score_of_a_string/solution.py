def solution(s: str) -> int:
    score = 0
    i = 1
    while i < len(s):
        score += abs(ord(s[i]) - ord(s[i-1]))
        i += 1

    return score
