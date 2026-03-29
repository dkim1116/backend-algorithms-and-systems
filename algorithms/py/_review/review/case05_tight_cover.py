from __future__ import annotations

# Tight Cover
#
# Given strings source and need, find the shortest substring of source that contains every character from need with the required counts.
# Return an empty string if no such substring exists.
#
# Input: source = 'ADOBECODEBANC', need = 'ABC'
# Output: 'BANC'
# Input: source = 'a', need = 'aa'
# Output: ''

class Solution:
    def solve(self, source: str, need: str) -> str:
        freqMap = {}

        for char in need:
            freqMap[char] = freqMap.get(char, 0) + 1

        required = len(need)
        start = 0
        minLength = float('inf')
        
        left = 0
        
        for right in range(len(source)):
            char = source[right]

            if char in freqMap:
                if freqMap[char] > 0:
                    required -= 1
                freqMap[char] -= 1

            while required == 0:
                if right - left + 1 < minLength:
                    start = left
                    minLength = min(minLength, right - left + 1)

                leftChar = source[left]

                if leftChar in freqMap:
                    freqMap[leftChar] += 1

                    if freqMap[leftChar] > 0:
                        required += 1

                left += 1

        return source[start:start + minLength] if minLength != float('inf') else ""


