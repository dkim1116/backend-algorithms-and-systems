from __future__ import annotations

# Target Runs
#
# Count how many contiguous subarrays sum to k.
# The array may contain positive, zero, and negative values.
#
# Input: nums = [1, 1, 1], k = 2
# Output: 2
# Input: nums = [1, 2, 3], k = 3
# Output: 2

class Solution:
    def solve(self, nums: list[int], k: int) -> int:
        sumMap = {0 : 1}
        runningSum = 0
        count = 0

        for num in nums:
            runningSum += num

            if runningSum - k in sumMap:
                count += sumMap[runningSum - k]

            sumMap[runningSum] = sumMap.get(runningSum, 0) + 1

        return count
