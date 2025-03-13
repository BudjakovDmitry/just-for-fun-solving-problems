from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    diffs = {}
    for i, n in enumerate(nums):
        if n in diffs:
            return [diffs[n], i]
        diff = target - n
        diffs[diff] = i
