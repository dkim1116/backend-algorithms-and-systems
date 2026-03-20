# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.


# Pattern:
#     Interval sweep and merge

# Approach:
#     I need to handle three cases:
#         - Interval is before the NewInterval:
#             - Simply Insert
#         - Interval overlaps with NewInterval
#             - Merge the Intervals
#         - Interval comes after the NewInterval
#             - Insert the NewInterval and then insert the Interval

# Time & Space complexity:
#     Time complexity is O(n) where n is the size of the intervals array
#     Space complexity is O(1) we always have newInterval to use for merging and result array doesn't get counted to the space complexity

# Edge Case(s):
#     If NewInterval comes at the end of all the intervals, this needs to be inserted


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart, newEnd = newInterval
        inserted = False

        intervals.sort(key=lambda x: x[0])

        for start, end in intervals:
            if end < newStart:
                result.append([start, end])
            elif start > newEnd:
                if not inserted:
                    result.append([newStart, newEnd])
                    inserted = True
                result.append([start, end])
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)

        if not inserted:
            result.append([newStart, newEnd])
        return result
        