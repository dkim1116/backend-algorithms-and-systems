# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Backtracking (inefficient for big inputs)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        result = 0

        def dfs(index, total):
            nonlocal result

            if index == len(coins) or total > amount:
                return
            if total == amount:
                result += 1

            for i in range(index, len(coins)):
                dfs(i, total + coins[i])
        dfs(0,0)
        return result

# Goal: I need to find the number of unique coin combinations that add up to the target amount.
# State: I track, for each amount, how many combinations can make that amount.
# Transition: For each coin, I go through every amount and check whether that coin can contribute to it. If it can, I add the number of combinations from current amount - coin, because I can extend all of those combinations with the current coin.
# Basecase: For amount 0, there is exactly 1 way to make it: choose nothing.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        state = [0 for _ in range(amount + 1)]
        state[0] = 1
        
        for coin in coins:
            for a in range(amount + 1):
                if a - coin >= 0:
                    state[a] += state[a - coin]
        
        return state[-1]