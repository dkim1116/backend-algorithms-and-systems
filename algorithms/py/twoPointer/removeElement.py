# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


# Pattern:
#     Two pointer swap

# Approach:
#     I use a read pointer to scan the array and a write pointer to track
#     where the next valid element should go.
#     If nums[readPointer] is not equal to val, I copy it to writePointer
#     and move writePointer forward.
#     At the end, writePointer is the number of elements kept.

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        readPointer = 0
        writePointer = 0

        while readPointer < len(nums):
            if nums[readPointer] != val:
                nums[readPointer], nums[writePointer] = nums[writePointer], nums[readPointer]
                writePointer += 1
            readPointer += 1
        return writePointer
            