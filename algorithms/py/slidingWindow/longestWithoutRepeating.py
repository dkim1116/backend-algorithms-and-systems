# Pattern: 
#     Sliding window (variable size)

# Approach:
#     We use a sliding window with a set to track characters in the current window.
#     As we expand the window, if we see a duplicate character, we shrink the window from the left until the duplicate is removed.
#     We update the maximum window length at each step.

# Time & Space complexity:
#     Time complexity is O(n) since each character is added and removed from the set at most once
#     Space complexity is O(n) as the hashmap can grow to size of n



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_set = set()

        left = 0

        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(char)

            longest = max(longest, right - left + 1)

        return longest