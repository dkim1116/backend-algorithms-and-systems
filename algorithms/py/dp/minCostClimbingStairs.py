# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.


# Pattern:
#     DP

# Approach:
#     In this problem at each step there is a cost and by paying the cost, we can climb either 1 or 2 stairs
#     I define dp[i] to get the optimal cost at every step
#     Base case will be:
#       Step 1 dp[0] = costs[0]
#       Step 2 dp[1] = costs[1]

#     At each step I check to see if I want to take cost from previous step or from two steps ago:
#       dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])

#     At the end, we can finish from the last step, or the step before the last step so we check:
#       min(dp[-1], dp[-2])

class Solution:
    def minCostClimbingStairs(self, costs: list[int]) -> int:
        dp = [0] * len(costs)

        for i in range(len(costs)):
            if i <= 1:
                dp[i] = costs[i]
            else:
                dp[i] = costs[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
    