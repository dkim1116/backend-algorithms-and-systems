# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = 0
        freqMap = {}
        left = 0

        for right, char in enumerate(s):

            freqMap[char] = freqMap.get(char, 0) + 1

            while len(freqMap) > k:
                leftChar = s[left]

                freqMap[leftChar] -= 1

                if freqMap[leftChar] == 0: del freqMap[leftChar]
                left += 1

            longest = max(longest, right - left + 1)

        return longest