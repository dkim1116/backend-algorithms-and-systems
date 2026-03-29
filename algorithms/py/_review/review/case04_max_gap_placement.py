from __future__ import annotations

# Max Gap Placement
#
# You are given basket positions on a number line.
# Place m balls so that the minimum distance between any two placed balls is as large as possible.
# Return that best possible minimum distance.
#
# Input: positions = [1, 2, 3, 4, 7], m = 3
# Output: 3
# Input: positions = [5, 4, 3, 2, 1, 1000000000], m = 2
# Output: 999999999

class Solution:
    def solve(self, positions: list[int], m: int) -> int:
        positions.sort()
        minDist = positions[1] - positions[0]
        maxDist = positions[-1] - positions[0]

        def works(dist):
            balls = 1
            prevDist = positions[0]

            for i in range(1, len(positions)):
                if positions[i] - prevDist >= dist:
                    balls += 1
                    prevDist = positions[i]
            return balls >= m
        
        left = minDist
        right = maxDist

        while left <= right:
            mid = (left + right) // 2

            if works(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
