# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class SolutionMemo:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def traverse(steps):
            if steps <= 1:
                return 1
            
            if steps not in memo:
                memo[steps] = traverse(steps - 1) + traverse(steps - 2)
            return memo[steps]
        
        return traverse(n)
    
class SolutionClassic:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i <= 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]