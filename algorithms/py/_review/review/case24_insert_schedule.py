from __future__ import annotations

# Insert Schedule
#
# You are given a list of non-overlapping intervals sorted by start time.
# Insert one new interval and merge if needed so the result remains non-overlapping and sorted.
#
# Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# Output: [[1, 5], [6, 9]]
# Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
# Output: [[1, 2], [3, 10], [12, 16]]

class Solution:
    def solve(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        newStart, newEnd = newInterval
        inserted = False

        for currStart, currEnd in intervals:
            if currEnd < newStart:
                result.append([currStart, currEnd])
            elif currStart > newEnd:
                if not inserted:
                    result.append([newStart, newEnd])
                    inserted = True
                result.append([currStart, currEnd])
            else:
                newStart = min(currStart, newStart)
                newEnd = max(currEnd, newEnd)

        if not inserted:
            result.append([newStart, newEnd])
        return result
