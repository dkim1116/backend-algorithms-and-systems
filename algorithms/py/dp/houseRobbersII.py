# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    def houseRobbers2(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def maxStolen(subNums) -> int:
            if len(subNums) == 1:
                return subNums[0]

            dp = [0] * len(subNums)

            dp[0] = subNums[0]
            dp[1] = max(subNums[0], subNums[1])

            for i in range(2, len(subNums)):
                dp[i] = max(dp[i - 1], subNums[i] + dp[i - 2])

            return dp[-1]
        
        return max(maxStolen(nums[:-1]), maxStolen(nums[1:]))

            