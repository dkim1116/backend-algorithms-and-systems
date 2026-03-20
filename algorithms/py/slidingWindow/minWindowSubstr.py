# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Pattern:
#    Sliding window (variable size)

# Approach:
#    We keep track of char freq of every character in string t and we decrease the freq of a character as we expand our window and increase as we shrink our window
#    We keep track of the actual required count of every character in string t with requiredCount and we decrease when new character in window is actually needed and increase when we shrink our window and the removed character was needed
#    When required == 0 we update the global minLength if its the shortest we've seen
#    If it is the shortest we've seen, we update the global start index with current left pointer. Result will be slicing string s from index start to start + minLength

# Time & Space complexity:
#    Time complexity will be O(n) since each character is considered at most twice when we expand and shrink the window
#    Space complexity will be O(n) as hashmap size can be at most n

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
