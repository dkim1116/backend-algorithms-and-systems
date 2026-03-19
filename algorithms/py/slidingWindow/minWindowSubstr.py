# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charFreq = {}

        for char in t:
            charFreq[char] = charFreq.get(char, 0) + 1

        minLength = None

        requiredCount = len(t)
        start = 0
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in charFreq:
                if charFreq[char] > 0:
                    requiredCount -= 1
                charFreq[char] -= 1
            
            while requiredCount == 0:
                currLength = right - left + 1

                if minLength is None or currLength < minLength:
                    minLength = currLength
                    start = left

                leftChar = s[left]

                if leftChar in charFreq:
                    charFreq[leftChar] += 1
                    if charFreq[leftChar] > 0:
                        requiredCount += 1

                left += 1

                

        return s[start:start + minLength] if minLength is not None else ""
