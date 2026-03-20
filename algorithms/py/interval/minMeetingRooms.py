# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Pattern:
#     Sort and Two pointer problem

# Approach:
#     We will map two arrays from intervals with start and end then sort in ascending order
#     Using two pointers, one for starts and one for ends, when starts[startIndex] < ends[endIndex] then we need a room and move the startIndex by 1
#     If ends[endIndex] <= starts[startIndex] then we can clean up a room then move the endIndex by 1
#     We always keep track of currentRoom count at any moment and update the maxRoom count 

# Time & Space complexity:
#     Time complexity is O(n log n) due to sorting
#     Space complexity is O(2n) where n is the size of intervals

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