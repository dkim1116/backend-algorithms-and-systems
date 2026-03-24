# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Pattern:
#     Binary Search on answer

# Approach:
#     I need to find the minimumSpeed needed for Koko to be able to finish all piles of bananas with unlimited time minSpeed = 1
#     I need to find the maximumSpeed needed for Koko to be able to finish any pile of bananas maxSpeed = max(piles)
#     This will be the range we run binary Search on [minSpeed, maxSpeed]
#     I find the middle speed between [minSpeed, maxSpeed] and check if Koko can finish all bananas at midSpeed within h hours
#     If she can finish, then I check if she can still finish within median speed of [minSpeed, midSpeed - 1]
#     If she can't then I check [midSpeed + 1, maxSpeed] because she needs to eat faster to be able to finish all bananas within h hours

# Time & Space complexity:
#     Time complexity is O(n log sum(piles)) n represents the length of piles and we will run binary search within range of (1, sum(piles))
#     Space complexity is O(1)

class Solution:
    def minEatingSpeed(self, piles: list[int], hours: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        def canFinish(speed):
            hour_used = 0

            for bananas in piles:
                hour_used += (bananas + speed - 1) // speed

            return hour_used <= hours
        
        left = minSpeed
        right = maxSpeed

        while left <= right:
            mid = (left + right) // 2

            if canFinish(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left