# 416. Partition Equal Subset Sum
# Given an integer array nums, 
# return true if you can partition the array into two subsets 
# such that the sum of the elements in both subsets is equal or false otherwise.

class SolutionDFS:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2
        memo = {}

        def dfs(index, remaining):
            nonlocal memo
            if index == len(nums) or remaining < 0:
                return False
            
            if remaining == 0:
                return True
            
            key = (index, remaining)
            if key in memo:
                return memo[key]
            
            take = dfs(index + 1, remaining - nums[index])
            skip = dfs(index + 1, remaining)
            
            memo[key] = take or skip
            return memo[key]
        
        return dfs(0, target)
    
class SolutionDP:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2
        state = [False for _ in range(target + 1)]
        state[0] = True

        for num in nums:
            next_state = state[:]

            for s in range(target + 1):
                if state[s] and s + num <= target:
                    next_state[s + num] = True

            state = next_state
        return state[-1]