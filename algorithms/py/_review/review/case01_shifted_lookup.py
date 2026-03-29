from __future__ import annotations

# Shifted Lookup
#
# A strictly increasing array was rotated once at an unknown pivot.
# Given the rotated array and a target value, return the target index or -1 if it is missing.
# Aim for logarithmic time.
#
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1

class Solution:
    def solve(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
            else:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid +1
        return -1
