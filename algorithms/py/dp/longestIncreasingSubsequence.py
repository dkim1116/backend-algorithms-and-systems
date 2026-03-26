# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# Pattern:
#     This is a dynamic programming problem because for each index, 
#     I want to determine the longest increasing subsequence that ends at that index, 
#     and I can build that using results from previous indices.

# State:
#     dp[i] = length of the longest increasing subsequence that ends at index i

# Initialization:
#     Every number by itself forms a valid increasing subsequence of length 1, so I initialize all values in dp to 1

# Transition:
#     For each index i, I look at all previous indices j
#     If nums[j] < nums[i], then I can extend the subsequence ending at j by including nums[i]
#     dp[i] = max(dp[i], dp[j] + 1)

# Result:
#     The longest increasing subsequence can end at any index, so the result is the maximum value in the dp array

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)