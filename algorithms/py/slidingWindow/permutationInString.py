# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Pattern:
#    Sliding window (fixed size)

# Approach:
#    We use a sliding window with hashmap to keep track of char freq of every char in s1
#    We update the char freq needed from hashmap as we expand and shrink our window
#    If requireCount that makes up for actual required characters in s1 == 0 then we return True

# Time & Space complexity:
#    Time complexity is O(n), where n is the length of s2, since each character is processed at most twice
#    Space complexity is O(m), where m is the number of distinct characters in s1

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap = {}

        for i in range(len(s1)):
            freqMap[s1[i]] = freqMap.get(s1[i], 0) + 1

        required = len(s1)
        left = 0

        for right in range(len(s2)):
            rightChar = s2[right]

            if rightChar in freqMap:
                if freqMap[rightChar] > 0:
                    required -= 1
                freqMap[rightChar] = freqMap.get(rightChar) - 1

            if right - left + 1 > len(s1):
                leftChar = s2[left]

                if leftChar in freqMap:
                    freqMap[leftChar] = freqMap.get(leftChar) + 1
                    if freqMap[leftChar] > 0:
                        required += 1
                left += 1
            
            if required == 0: return True
        
        return False

# "abc" "abbc" 