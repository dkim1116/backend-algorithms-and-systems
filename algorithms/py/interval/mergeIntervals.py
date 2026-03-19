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