from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        totalRain = 0
        leftMax = 0
        rightMax = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] < heights[right]:
                if heights[left] > leftMax:
                    leftMax = heights[left]
                else:
                    totalRain += leftMax - heights[left]
                left += 1
            else:
                if heights[right] > rightMax:
                    rightMax = heights[right]
                else:
                    totalRain += rightMax - heights[right]
                right -= 1
        
        return totalRain