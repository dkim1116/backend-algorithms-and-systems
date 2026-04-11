# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# Pattern:
#     DP

# Approach:
#     Every house that we consider, we need to see if robbing this house + the 2 houses before is more money than robbing just previous house
#     First house we don't have other candidates so we set this one as the maximum we can rob
#     Second house we can compare to the previous house which one is worth more 
#     Third house and onward we compare if robbing the current house + previous non adjacent houses are worth morth than the previous house + the non adjacent ones to them
#     Return the last sum

# Time & Space complexity:
#     Time complexity is O(n) where we consider houses of input array size
#     Space complexity is O(n) as we keep track of highest possible sum of money for every house

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]