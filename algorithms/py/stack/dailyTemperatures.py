from typing import List

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result = [0] * len(temps)
        stack = []

        for i in range(len(temps)):
            temp = temps[i]

            while len(stack) and temp > temps[stack[-1]]:
                prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex

            stack.append(i)

        return result