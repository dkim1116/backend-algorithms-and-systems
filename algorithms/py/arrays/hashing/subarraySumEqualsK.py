# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Pattern:
#     This is a prefix sum with hashmap problem

# Approach:
#     I keep track of the runningSum in a hashmap as I iterate through the array of integers.
#     If currentRunningSum - previousRunningSum = k then we have a subarray where the sum equals to k
#     To find the previousRunningSum we compute currentRunningSum - k = previousRunningSum and check for the previousRunningSum in hashmap
#     We keep track of the frequency of runningSum in the hashmap because the same runningSum can appear multiple times and each occurrence
#     represents a different starting point for a valid subarray

# Time & Space complexity:
#     Time complexity of this is linear O(n)
#     Space complexity is O(n) for the hashmap we use to keep track of runningSums

# EdgeCase(s):
#     If the first number matches k then we need to be able to find currentRunningSum - k = 0 in hashmap



class Solution:
    def subArraySum(self, nums: list[int], k: int) -> int:
        hashmap = {0: 1}
        runningSum = 0
        count = 0

        for i, num in enumerate(nums):
            # currentSum - previousSum = k
            # currentSum - k = previousSum
            runningSum += num

            if runningSum - k in hashmap:
                count += hashmap[runningSum - k]

            hashmap[runningSum] = hashmap.get(runningSum, 0) + 1

        return count