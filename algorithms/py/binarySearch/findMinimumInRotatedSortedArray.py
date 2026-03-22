# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Pattern:
#     Binary Search

# Approach:
#     I use left and right pointer to check subarrays of the input array
#     Ex: [3,4,5,1,2] mid = 5 comparing mid to left is always ascending order. So we compare mid to right to check if the array was rotated
#     If mid >= right then we search right else we search left for the smallest number
#     We continue until left == right

# Time & Space complexity:
#     Time complexity is O(log n)
#     Space complexity is O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]