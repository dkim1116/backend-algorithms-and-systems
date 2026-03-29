from __future__ import annotations

# Hidden Anagram
#
# Return True if any substring of s2 is a permutation of s1.
# Otherwise return False.
#
# Input: s1 = 'ab', s2 = 'eidbaooo'
# Output: True
# Input: s1 = 'ab', s2 = 'eidboaoo'
# Output: False

class Solution:
    def solve(self, s1: str, s2: str) -> bool:
        freqMap = {}

        for char in s1:
            freqMap[char] = freqMap.get(char, 0) + 1

        needed = len(s1)
        left = 0

        for right in range(len(s2)):
            char = s2[right]

            if char in freqMap:
                if freqMap[char] > 0:
                    needed -= 1
                freqMap[char] -= 1

            while right - left + 1 > len(s1):
                leftChar = s2[left]

                if leftChar in freqMap:
                    freqMap[leftChar] += 1

                    if freqMap[leftChar] > 0:
                        needed += 1
                left += 1

            if needed == 0:
                return True
        return False

