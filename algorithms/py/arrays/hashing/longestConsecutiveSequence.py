from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                count = 1

                while num + count in num_set:
                    count += 1

                longest = max(longest, count)

        return longest