# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Pattern:
#     Simple binary search

# Approach:
#     I use a left and right index from start and end of the input array then always look at the middle element to compare to the target
#     If the middle number is smaller than target, we move the left index to middle + 1 to look at the right half of the array
#     Repeat this process until we find the number or we exceed the array

# Time & Space complexity:
#     Time complexity is O(log n) where n is the size of the input array
#     Space complexity is O(1) as we only using left and right index pointer to find the index

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

        return -1