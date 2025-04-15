from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    numbers = sorted(nums)
    target = None
    result = []
    n = len(numbers)
    for i in range(n):
        left = right = None
        # current_target == previous_target. Skip it.
        if numbers[i] == target:
            continue

        target = numbers[i]
        # two pointers
        j = i + 1
        k = n - 1
        while j < k:
            # current left pointer == previous left pointer. Skip it.
            if numbers[j] == left:
                j += 1
                continue
            # current right pointer == previous right pointer. Skip it.
            if numbers[k] == right:
                k -= 1
                continue

            left = numbers[j]
            right = numbers[k]
            sum_ = target + left + right
            if sum_ < 0:
                j += 1
                right = None
            elif sum_ > 0:
                k -= 1
                left = None
            else:
                result.append([target, left, right])
                j += 1
                k -= 1

    return result