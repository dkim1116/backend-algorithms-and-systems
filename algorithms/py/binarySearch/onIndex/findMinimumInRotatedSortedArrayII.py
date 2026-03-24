# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

# You must decrease the overall operation steps as much as possible.

# Pattern:
#     Binary Search

# Approach:
#     I will use [left, right] point to look at subarrays of the input
#     When mid < right we look to the left half
#     If mid > right we look to the right half
#     If mid == right then we shrink from right

# Time & Space complexity:
#     Time complexity O(log n)
#     Space complexity O(1)

Edge case(s):
    # 1. [4,4,5,0,1] left = 0 right = 4, mid = 2 midInt = 5
    #     5 > 1 so we look to the right half
    #     left = 3, right = 4 mid = 3 midInt = 0
    #     0 < 1 so we look to the left half
    #     left = 3, right = 3 mid = 3
    #     left == right return mid
    # 2.  [0,0,1,2,3] left = 0 right = 4 mid = 2 midInt = 1
    #     1 < 3 so we look to the left half
    #     left = 0 right = 2 mid = 1 midInt = 0
    #     0 < 1 so we look to the left half
    #     left = 0 right = 1 mid = 0 midInt = 0
    #     * 0 <= 0 so we look to the left half. We need to be aware when midInt <= right int and look left
    #     left == right return mid
    # 3. [3,1] left = 0 right = 1 mid = 0 midInt = 3
    #     3 > 1 so we look right
    #     left = 1 right = 1 mid = 1 midInt = 1
    #     return mid


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]
