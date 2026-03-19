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