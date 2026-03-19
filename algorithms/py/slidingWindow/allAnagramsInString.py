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