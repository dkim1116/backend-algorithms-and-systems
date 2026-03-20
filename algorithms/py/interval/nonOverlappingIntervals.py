# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# Pattern:
    # Sort and Greedy

# Approach:
    # We first sort the intervals by start time so that overlapping intervals will be positioned next to each other
    # We sweep through the intervals while keeping track of lastEnd (previous interval's endTime) 
    # If the current interval overlaps (start < prevEnd), we remove one interval
    # by keeping the one with the smaller end.
    # Otherwise, we update prevEnd to the current end.

# Time & Space complexity:
#     Time complexity is O(n log n) due to sorting
#     Space complexity is O(1) as we only keep track of removed count and the prevEnd

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort(key=lambda x: x[0])
        prevEnd = None

        for start, end in intervals:
            if prevEnd is None:
                prevEnd = end
                continue

            if start < prevEnd:
                prevEnd = min(prevEnd, end)
                removed += 1
            else:
                prevEnd = end

        return removed