from __future__ import annotations

# Bloom Deadline
#
# flowers[i] is the day the i-th flower opens.
# Build m bouquets using exactly k adjacent open flowers per bouquet.
# Return the minimum day when this becomes possible, or -1 if it never can.
#
# Input: flowers = [1, 10, 3, 10, 2], m = 3, k = 1
# Output: 3
# Input: flowers = [1, 10, 3, 10, 2], m = 3, k = 2
# Output: -1

class Solution:
    def solve(self, flowers: list[int], m: int, k: int) -> int:
        if m * k > len(flowers):
            return -1

        minDays = min(flowers)
        maxDays = max(flowers)


        def works(days):
            bouquet = 0
            currFlower = 0

            for flower in flowers:
                if flower <= days:
                    currFlower += 1

                    if currFlower == k:
                        bouquet += 1
                        currFlower = 0
                else:
                    currFlower = 0
            return bouquet >= m

        left = minDays
        right = maxDays

        while left <= right:
            mid = (left + right) // 2

            if works(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
