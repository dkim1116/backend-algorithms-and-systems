from typing import List

class Solution:
    def subArraySum(self, nums: List[int], k: int) -> int:
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