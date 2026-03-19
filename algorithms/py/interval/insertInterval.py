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
        