from typing import List


def concatenation(nums: List[int]) -> List[int]:
    nums.extend(nums)
    return nums
