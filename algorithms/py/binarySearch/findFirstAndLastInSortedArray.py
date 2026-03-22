# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Pattern:
#     Binary Search 

# Approach:
#     I use binary search to find the starting index of a target and the end separately
#     I use left and right pointer to keep track of the subarray we are searching
#     We find the middle of the array to check if we want to search the first half or left half
#     Even when we find the target, we keep moving left to find the start and moving right to find the end

# Time & Space complexity:
#     Time complexity is O(2 log n) where n is the length of the array and 2 gets added as we need to run the algorith to find starting and ending position
#     Space complexity is O(1) as we only use left and right pointer

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch(True, nums, target)
        right = self.binSearch(False, nums, target)
        return [left, right]
    
    def binSearch(self, bnFindLeft: bool, nums: list[int], target:int) -> int:
        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid

                if bnFindLeft:
                    right = mid - 1
                else:
                    left = mid + 1

        return index