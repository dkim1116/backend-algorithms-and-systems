from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_set = set()

        left = 0

        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(char)

            longest = max(longest, right - left + 1)

        return longest