# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Pattern:
#     Kadane's algorithm (DP with Greedy)

# Approach:
#     At each position, track the maximum and minimum product of any subarray ending at that index.
#     We need both because multiplying by a negative number can flip the smallest product into the largest.
#     For each number, the new max/min product ending here can come from:
#         1. starting fresh from the current number
#         2. current number * previous max product
#         3. current number * previous min product
#     The overall answer is the largest max product seen across the array.

class Solution:
    def maxProductSubarray(self, nums: list[int]) -> int:
        maxEnding = nums[0]
        minEnding = nums[0]
        best = nums[0]

        for num in nums[1:]:
            prevMax = maxEnding
            prevMin = minEnding

            maxEnding = max(num, num * prevMax, num * prevMin)
            minEnding = min(num, num * prevMax, num * prevMin)
            best = max(best, maxEnding)

        return best