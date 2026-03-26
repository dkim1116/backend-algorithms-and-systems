# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0


# Pattern:
#     Brute-force solution is to use backtracking and finding combination sums
#     Optimized solution is to use DP as we are looking for minimum combinations, not all

# Approach:
#     I build the answer from smaller amounts to bigger amounts.
#     dp[i] tells me the fewest coins needed to make amount i.
#     For each amount, I try every coin and ask: if this coin is the last one I use, what smaller amount is left?
#     If I already know the best answer for that smaller amount, I add one for the current coin.
#     I try all coins and keep the minimum.

# Edge case(s):
#     I need to start with base case of 0 amount as it takes no coins to make up for 0

#     To make sure we can correctly find the minimum across all coin combinations at every amount, we initialize dp with infinity

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1