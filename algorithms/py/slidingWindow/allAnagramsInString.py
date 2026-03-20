# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# Pattern:
#    This is a fixed-size sliding window problem

# Approach:
#    I build a frequency hashmap for the characters in t.
#    Then I slide a window over s and decrease the count for each character that enters the window.
#    I keep track of how many characters are still needed using requiredCount, which starts at len(t).
#    If a character is still needed, I decrement requiredCount.
#    Once the window grows larger than len(t), I shrink it from the left and restore the frequency count.
#    If removing a character makes it needed again, I increment requiredCount.
#    Whenever requiredCount becomes 0, the current window is an anagram, so I add left to the result.

# Time & Space complexity:
#    Time complexity is O(n), where n is the length of s, because each character enters and leaves the window at most once.
#    Space complexity is O(m), where m is the number of distinct characters in t.

# Edge case(s):
#    Handle when len(t) > len(s)



class Solution:
    def allAnagrams(self, s: str, t: str) -> list[int]:
        result = []
        charFreq = {}

        for i, char in enumerate(t):
            charFreq[char] = charFreq.get(char, 0) + 1

        requiredCount = len(t)
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in charFreq:
                if charFreq[char] > 0:
                    requiredCount -= 1
                charFreq[char] -= 1

            if right - left + 1 > len(t):
                leftChar = s[left]

                if leftChar in charFreq:
                    charFreq[leftChar] += 1
                    if charFreq[leftChar] > 0:
                        requiredCount += 1
                left += 1

            if requiredCount == 0:
                result.append(left)

        return result