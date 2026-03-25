# Given an integer array nums, find the subarray with the largest sum, and return its sum.


# Pattern:
#     Kadane's algorithm (DP with Greedy)

# Approach:
#     At any given position as we iterate through the input array, we need to track:
#         - Is subarray upto current position give best sum? Or should we start a new one?
#         - Is this current subarray best we've seen yet?

class Solution:
    def maxSubarraySum(self, nums: list[int]) -> int:
        current = nums[0]
        best = nums[0]

        for num in nums[1:]:
            current = max(current + num, num)
            best = max(best, current)

        return best
