from typing import List

# Brute force
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)

        for i in range(n):
            height = heights[i]

            left = i
            while left >= 0 and heights[left] >= height:
                left -= 1

            right = i
            while right < n and heights[right] >= height:
                right += 1

            width = right - left - 1
            maxArea = max(maxArea, width * height)

        return maxArea
        

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights) + 1):
            currHeight = 0 if i == len(heights) else heights[i]

            while stack and currHeight < heights[stack[-1]]:
                height = heights[stack.pop()]
                leftBoundary = stack[-1] if stack else -1
                width = i - leftBoundary - 1
                maxArea = max(maxArea, width * height)

            stack.append(i)

        return maxArea