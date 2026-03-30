from __future__ import annotations

# Common Items
#
# Return the k values that appear most often in the array.
# You may return them in any order.
#
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def solve(self, nums: list[int], k: int) -> list[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0)
            freqMap[num] += 1

        freqBucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            freqBucket[freq].append(num)

        res = []

        for i in reversed(range(len(nums))):
            for num in freqBucket[i]:
                res.append(num)

                if len(res) == k:
                    return res