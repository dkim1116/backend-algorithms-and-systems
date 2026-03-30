from __future__ import annotations

# Collapse Ranges
#
# Given a list of intervals, merge all overlapping ranges.
#
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Input: intervals = [[1, 4], [4, 5]]
# Output: [[1, 5]]

class Solution:
    def solve(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []

        intervals.sort()

        for currStart, currEnd in intervals:
            if not result:
                result.append([currStart, currEnd])
            else:
                prevStart, prevEnd = result[-1]

                maxStart = max(prevStart, currStart)
                minEnd = min(prevEnd, currEnd)

                if maxStart <= minEnd:
                    result[-1] = [prevStart, max(prevEnd, currEnd)]
                else:
                    result.append([currStart, currEnd])
        return result
