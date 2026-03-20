# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# This is a hashset problem where I start the count for the longest sequence where I find the start of a sequence.
# My intuition for this problem is that I would add the entire array of integers into a set
# Then I iterate through the set and when I find a number that does not have a number - 1 in the set, I would start going through
# the set while counting how long the sequence is. When I am done counting, I would check the global count to see if it's the longest we've seen

# Time complexity of this needs to O(n) as we visit each number at most once 
# Space complexity would be N as we use a hashset to look up numbers with constant time complexity

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                count = 1

                while num + count in num_set:
                    count += 1

                longest = max(longest, count)

        return longest