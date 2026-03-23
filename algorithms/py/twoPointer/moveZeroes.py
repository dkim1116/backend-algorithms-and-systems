# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Pattern:
#     Two pointer swap problem

# Approach:
#     I point both read and write to start of array
#     If read element is not 0, then we swap with write pointer then move the write pointer
#     I always move the read pointer by 1



class Solution:
    def moveZeros(self, nums: list[int]) -> list[int]:
        readPointer = 0
        writePointer = 0

        while readPointer < len(nums):
            if nums[readPointer] != 0:
                nums[readPointer], nums[writePointer] = nums[writePointer], nums[readPointer]
                writePointer += 1
            readPointer += 1
            
        return nums