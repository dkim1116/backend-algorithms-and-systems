# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

# Pattern:
#    Sliding window (variable size)

# Approach:
#    We use a sliding window and a hashmap to keep track of characters inside the window
#    We expand window while updating global longest length until we have a hashmap size > k
#    When hashmap size > k we start shrinking the window from left and remove the char from hashmap if freq becomes 0

# Time & Space complexity:
#    Time complexity is O(n) as we look at every char at most twice when we expand and shrink our window
#    Space complexity is O(k) as hashmap can grow upto size k

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