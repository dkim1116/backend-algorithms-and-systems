# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Pattern: 
#    This is a variable-sized sliding window problem

# Approach:
#    As we expand our window to the right, we will keep track of char frequency in a hashmap and update global mostFreqCount if it is the most frequent character in window
#    If windowSize - mostFreqCount > k then we need to shrink our window from left until windowSize - mostFreqCount <= k
#    When we shrink our window from left, we need to update the char frequency map
#    We will update global longest window length if it is the longest window we've seen yet

# Time & Space complexity:
#    Time complexity is O(n) as we go over a number at most twice when we expand and shrink our window
#    Space complexity is O(n) as the hashmap can grow n size

# Edge case(s):


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {}

        mostFreqCount = 0
        longest = 0
        left = 0

        for right in range(len(s)):
            char = s[right]

            charFreq[char] = charFreq.get(char, 0) + 1
            mostFreqCount = max(mostFreqCount, charFreq[char])

            while right - left + 1 - mostFreqCount > k:
                leftChar = s[left]
                charFreq[leftChar] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest