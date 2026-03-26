# Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

# Note that the subarray needs to be non-empty after deleting one element.

# Pattern:
#     Kadane's algorithm (DP with Greedy)

# Approach:
#     Standard Kadane tracks the maximum subarray sum ending at the current index.
#     At each number, we decide whether to start a new subarray from the current number or extend the previous subarray.
#
#     For this problem, we are allowed to delete at most one element so we track two states:
#         - noDel: maximum subarray sum ending at the current index with no deletion used
#         - oneDel: maximum subarray sum ending at the current index with one deletion used
#
#         - noDel = max(num, prevNoDel + num)
#           -> either start fresh or extend previous subarray with no deletion
#
#         - oneDel = max(prevNoDel, prevOneDel + num)
#           -> either delete the current number and take previous noDel,
#              or keep the current number and extend a subarray where deletion was already used
#
#     The answer is the best value seen among noDel and oneDel across the array.

# Pattern:
#     Dynamic Programming as we compute the max sum at any given index with previous answers ending at given index

# State:
#     I need to keep track of two states. noDeleteBest and oneDeleteBest
#     noDeleteBest will check if previous answer + current num is best or just starting from current number
#     oneDeleteBest will check if previous answer is best or previous answer with one deletion + current number

# Initialization:
#     I start with the first item in array as thats the best one we've seen so far

# Transition:
#     Iterate through the array:
#         noDelBest = max(noDelBest + num, num)
#         oneDelBest = max(noDelBest, oneDelBest + num)

# Result:

class Solution:
    def maxSubarrayWithDeletion(self, nums: list[int]) -> int:
        noDelSum = nums[0]
        oneDelSum = float("-inf")
        best = nums[0]

        for num in nums[1:]:
            prevNoDel = noDelSum
            prevOneDel = oneDelSum

            noDelSum = max(prevNoDel + num, num)
            oneDelSum = max(prevOneDel + num, prevNoDel)

            best = max(best, oneDelSum, noDelSum)
        return best

