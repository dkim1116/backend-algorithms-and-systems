# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


# Pattern:
#     Two pointers

# Approach:
#     Because duplicates are positioned next to each other in the input array, we will use index - 1 to check for duplicates
#     I use readIndex and writeIndex starting at position 1, so I can directly compare if readIndex == writeIndex - 1 number
#     WriteIndex will have the first position where I can write to so writeIndex - 1 is where I check for duplicates
#     I continue moving readIndex until I stop seeing a duplicate number then I swap the position of readIndex number and writeIndex number then move the writeIndex
#     Where writeIndex stops is how many unique characters we have

class Solution:
    def removeDupes(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        readIndex = 1
        writeIndex = 1

        while readIndex < len(nums):
            if nums[readIndex] != nums[writeIndex - 1]:
                nums[readIndex], nums[writeIndex] = nums[writeIndex], nums[readIndex]
                writeIndex += 1
            readIndex += 1
        return writeIndex