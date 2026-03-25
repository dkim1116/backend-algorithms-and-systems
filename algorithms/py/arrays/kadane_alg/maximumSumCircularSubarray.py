# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


# Pattern:
#     Kadane's algorithm (DP with Greedy)

# Approach:
#     If the best sum doesn't wrap around the array, then standard Kadane's algorith will give us the answer.
#     If the best sum does wrap around the array, then the total sum of the array - minimum sum will give us the answer.
#     I need to keep track of best sum so far and minimum sum we've seen so far.
#     We will compute whether starting sum from current or extending from previous subarray is the maximum/minimum
#     Then we will check if bestSum or totalSum - minSum is the maximumSum.

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        totalSum = sum(nums)
        minSum = minCurrent = nums[0]
        maxSum = maxCurrent = nums[0]
        
        for num in nums[1:]:
            minCurrent = min(num, minCurrent + num)
            maxCurrent = max(num, maxCurrent + num)

            minSum = min(minSum, minCurrent)
            maxSum = max(maxSum, maxCurrent)

        if maxSum < 0:
            return maxSum
        
        return max(maxSum, totalSum - minSum)