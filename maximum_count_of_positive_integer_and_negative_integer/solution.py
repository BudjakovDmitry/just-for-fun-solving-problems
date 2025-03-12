from typing import List


def maximum_count(nums: List[int]) -> int:
    neg = 0
    zeros = 0
    for n in nums:
        if n < 0:
            neg += 1
        elif n == 0:
            zeros += 1
        else:
            break

    pos = len(nums) - neg - zeros
    return max((neg, pos))