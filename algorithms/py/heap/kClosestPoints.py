# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Pattern:
#     Heap problem

# Approach:
#     I use a maxHeap to keep k number of points in the heap. 
#     When the size exceeds k, we remove the furthest point from the top of the heap

# Time & Space complexity:
#     Time complexity is O(n log k) where n represents the number of points and k represents the size
#     Space complexity is O(k) as at most we keep size k in the heap

import heapq

class Solution:
    def kClosestPoints(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []

        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            heapq.heappush(maxHeap, (-distance, point))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [point for dist, point in maxHeap]