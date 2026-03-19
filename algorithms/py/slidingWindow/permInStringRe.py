# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def permInString(self, s1: str, s2: str) -> bool:
        charFreq = {}

        for char in s1:
            charFreq[char] = charFreq.get(char, 0) + 1

        required = len(s1)
        left = 0

        for right in range(len(s2)):
            char = s2[right]

            if char in charFreq:
                if charFreq[char] > 0: required -= 1
                charFreq[char] -= 1

            while right - left + 1 > len(s1):
                leftChar = s2[left]

                if leftChar in charFreq:
                    charFreq[leftChar] += 1
                    if charFreq[leftChar] > 0: required += 1

                left += 1

            if required == 0: return True
        return False
