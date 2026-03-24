# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

# Pattern:
#     Binary Search on answer

# Approach:
#     I find the minimum days needed for flowers to bloom min(bloomDays) and maximum days needed for all flowers to bloom max(bloomDays)
#     I run a binary search on this range [minBloomDays, maxBloomDays] and find the median in this range
#     If medBloomDays is enough to create the bouquets that we need, we look at the left half of the range [minBloomDays, medBloomDays - 1] else [medBloomDays + 1, maxBloomDays]
#     I check if we can create the bouquets we need by checking adjacent flowers as we iterate through the inputArray and 
#         if the adjacent flower count == k then bouquetCount += 1 and we reset adjacent flower count = 0
#         if the flowers dont bloom on current day, we reset adjacent flower count = 0
#         if bouquetCount >= m then return True else False

# Time & Space complexity:
#     Time complexity is O (n log (max(bloomDays) - min(bloomDays))) 
#         - n is the length of bloomDays that we iterate over each time to check if we can make the bouquets needed, and we run BS on range max(bloomDays) - min(bloomDays)
#     Space complexity is O(1)

class Solution:
    def minDays(self, bloomDays: list[int], bouquetCount: int, flowerCount: int) -> int:
        if bouquetCount * flowerCount > len(bloomDays): return -1

        minBloomDays = min(bloomDays)
        maxBloomDays = max(bloomDays)

        def canMake(days):
            numBouquets = 0
            adjacentFlowers = 0

            for bloomDay in bloomDays:
                if bloomDay <= days:
                    adjacentFlowers += 1
                else:
                    adjacentFlowers = 0

                if flowerCount == adjacentFlowers:
                    numBouquets += 1
                    adjacentFlowers = 0
            return numBouquets >= bouquetCount
        
        left = minBloomDays
        right = maxBloomDays

        while left <= right:
            mid = (left + right) // 2

            if canMake(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left