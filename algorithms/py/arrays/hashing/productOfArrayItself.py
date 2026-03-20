# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all 
# the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Pattern:
# This is a prefix/suffix product problem

# Approach:
# I use two passes: first to build prefix products, then multiply in suffix products in reverse.

# Time/Space complexity:
# Time complexity of this approach is linear O(n)
# Space complexity is constant O(1) and the result array isn't counted

# Edge Case(s):
# Handle zeroes and do not use division



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