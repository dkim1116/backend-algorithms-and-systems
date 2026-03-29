from __future__ import annotations

# Full Arrangements
#
# Return every possible ordering of the given distinct integers.
#
# Input: nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Input: nums = [0, 1]
# Output: [[0, 1], [1, 0]]

class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(index):
            if index == len(nums):
                result.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        dfs(0)
        return result