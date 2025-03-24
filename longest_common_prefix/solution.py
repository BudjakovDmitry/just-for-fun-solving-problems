from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    prefix = ""
    for letters in zip(*strs):
        letters = set(letters)
        if len(letters) > 1:
            break
        prefix += letters.pop()

    return prefix