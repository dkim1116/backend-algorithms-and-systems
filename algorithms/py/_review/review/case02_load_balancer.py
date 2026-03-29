from __future__ import annotations

# Load Balancer
#
# You must split an array into exactly k non-empty contiguous groups.
# The score of a split is the largest group sum.
# Return the smallest possible score across all valid splits.
#
# Input: nums = [7, 2, 5, 10, 8], k = 2
# Output: 18
# Input: nums = [1, 2, 3, 4, 5], k = 2
# Output: 9

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        minSum = max(nums)
        maxSum = sum(nums)

        def canSplit(newSum):
            arr = 1
            currSum = 0

            for num in nums:
                if currSum + num > newSum:
                    arr += 1
                    currSum = num
                else:
                    currSum += num
            
            return arr <= k
        
        left = minSum
        right = maxSum

        while left <= right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
