# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Pattern:
#     Sort and sweep

# Approach:
#     We iterate through the intervals as we add to the result
#     If last item in the result overlaps with the current interval, we merge it

# Time & Space complexity:
#     Time complexity is O(n) where n is the size of intervals array
#     Space complexity is O(1) as we only use result array and we don't consider that in the space complexity

class Solution:
    def merge(self, intervals:list[list[int]]) -> list[list[int]]:
        result = []

        intervals.sort(key=lambda x: x[0])

        for start, end in intervals:
            if not result:
                result.append([start, end])
                continue

            lastStart, lastEnd = result[-1]

            if start <= lastEnd:
                lastEnd = max(end, lastEnd)
                result[-1] = [lastStart, lastEnd]
            else:
                result.append([start, end])

        return result