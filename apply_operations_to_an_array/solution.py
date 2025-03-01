from typing import List


class Solution:
    @staticmethod
    def shift_zeros(nums: List[int]) -> List[int]:
        result = []
        from_index = 0
        zeros = 0
        for i, n in enumerate(nums, start=1):
            if n == 0:
                result.extend(nums[from_index:i-1])
                from_index = i
                zeros += 1

        result.extend(nums[from_index:len(nums)])
        result.extend([0]*zeros)
        return result

    @classmethod
    def apply_operations(cls, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            i += 1

        return cls.shift_zeros(nums)
