from __future__ import annotations

# Uniform Stretch
#
# You may replace at most k characters in a string.
# Return the length of the longest substring that can be turned into one repeated letter after those replacements.
#
# Input: s = 'ABAB', k = 2
# Output: 4
# Input: s = 'AABABBA', k = 1
# Output: 4

class Solution:
    def solve(self, s: str, k: int) -> int:
        freqMap = {}

        maxLength = 0
        mostFreq = 0

        left = 0

        for right in range(len(s)):
            char = s[right]

            freqMap[char] = freqMap.get(char, 0) + 1
            mostFreq = max(mostFreq, freqMap[char])

            while (right - left + 1) - mostFreq > k:
                leftChar = s[left]
                freqMap[leftChar] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)
        return maxLength

