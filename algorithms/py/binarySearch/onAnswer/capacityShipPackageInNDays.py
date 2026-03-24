# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Pattern:
#     Binary Search on answer

# Approach:
#     I first find the min capacity possible max(minCapacity, weights[i]) and max capacity sum(weights)
#     I create a helper function that tells us whether we can achieve shipping all packages within specified days using a capacity
#     The range in binary search we will use will be minCapacity and maxCapacity
#     Every time we search, we will look at the median capacity between the two then check if we can ship all packages with this capacity
#     If possible, then we will look from [minCapacity, medianCapacity - 1] else [medianCapacity + 1, maxCapacity]
#     We repeat until we find the most optimal capacity then return

# Time & Space complexity:
#     Time complexity is (n log sum(weights))
#     Space complexity is O(1)


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        minCapacity = max(weights)
        maxCapacity = sum(weights)

        def canShip(capacity):
            days_used = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_used += 1
                    current_load = weight
                else:
                    current_load += weight

            return days_used <= days
        
        left = minCapacity
        right = maxCapacity

        while left <= right:
            mid = (left + right) // 2

            if canShip(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left