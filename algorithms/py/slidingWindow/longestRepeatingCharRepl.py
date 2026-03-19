# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

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