class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)

        maxRooms = 0
        currentRooms = 0
        startPointer = 0
        endPointer = 0

        while (startPointer < len(starts)):
            if (starts[startPointer] >= ends[endPointer]):
                currentRooms -= 1
                endPointer += 1

            currentRooms += 1
            maxRooms = max(maxRooms, currentRooms)

            startPointer += 1

        return maxRooms