# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Pattern:
#     This is a complement and hashmap problem

# Approach:
#     I iterate through the array and compute the complement (target - current number).
#     If the complement exists in the hashmap, I return the stored index and the current index.
#     Otherwise, I store the current number and its index in the hashmap.

# Time & Space complexity:
#     Time complexity is O(n)
#     Space complexity is O(n)

# Edge Case(s):
#     Handle duplicate numbers at different index

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[num] = i

        return []