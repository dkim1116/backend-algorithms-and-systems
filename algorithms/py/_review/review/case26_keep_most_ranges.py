from __future__ import annotations

# Keep Most Ranges
#
# Given a list of intervals, remove the fewest intervals so the remaining ones do not overlap.
# Return the number removed.
#
# Input: intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# Output: 1
# Input: intervals = [[1, 2], [1, 2], [1, 2]]
# Output: 2

class Solution:
    def solve(self, intervals: list[list[int]]) -> int:
        removed = 0
        prevEnd = None

        intervals.sort()

        for start, end in intervals:
            if prevEnd is None:
                prevEnd = end
                continue

            if start < prevEnd:
                removed += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end

        return removed
