from __future__ import annotations

# Streak Length
#
# Given an unsorted list of integers, return the length of the longest run of consecutive values.
# Your solution should be near linear time.
#
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9

class Solution:
    def solve(self, nums: list[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                currNum = num

                while currNum + 1 in numSet:
                    count += 1
                    currNum = currNum + 1
                
                maxLength = max(count, maxLength)
        return maxLength
