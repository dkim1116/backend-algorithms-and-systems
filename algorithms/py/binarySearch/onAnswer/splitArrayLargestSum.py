# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

# Pattern:
#     Binary search on answer

# Approach:
#     I find the minimum number we can split with minSum = max(nums)
#     I find the maximum number we can split with maxSum = sum(nums)
#     I run a binary search on range [minSum, maxSum] and get the medianSum from the range
#     I run through the nums array and see if we can split the array in k size and still fit each subarray sums within medianSum
#     If we can, we search the left half [minSum, medSum - 1] else [medSum + 1, maxSum]

# Time & Space complexity:
#     Time complexity is O(n log (sum(nums) - max(nums))) where n is the size of input array, and we run a binary search on range [max(nums), sum(nums)]
#     Space complexity is O(1)

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        minSum = max(nums)
        maxSum = sum(nums)

        def canSplit(totalSum):
            size = 1
            currentSum = 0

            for num in nums:
                if currentSum + num > totalSum:
                    size += 1
                    currentSum = num
                else:
                    currentSum += num
            return size <= k
        
        left = minSum
        right = maxSum

        while left <= right:
            med = (left + right) // 2

            if canSplit(med):
                right = med - 1
            else:
                left = med + 1
        return left