from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1

        for i in range(len(nums))
            result[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            result[i] *= prefix
            prefix *= num

        suffix = 1
        for i in reversed(range(len(nums))):
            result[i] *= suffix
            suffix *= nums[i]

        return result