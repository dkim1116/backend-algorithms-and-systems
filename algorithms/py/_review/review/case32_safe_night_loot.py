from __future__ import annotations

# Safe Night Loot
#
# You plan to rob houses along a street.
# Adjacent houses cannot both be robbed.
# Return the maximum money you can collect.
#
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Input: nums = [2, 7, 9, 3, 1]
# Output: 12

class Solution:
    def solve(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]
