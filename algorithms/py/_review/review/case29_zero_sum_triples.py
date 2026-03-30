from __future__ import annotations

# Zero Sum Triples
#
# Return all unique triplets [a, b, c] such that a + b + c == 0.
# Do not include duplicate triplets.
#
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Input: nums = [0, 1, 1]
# Output: []

class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]: continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: 
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result