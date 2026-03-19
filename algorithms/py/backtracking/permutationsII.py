# Flag check

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        used = [False] * len(nums)
        nums.sort()

        def dfs(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i] == True: 
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                path.append(nums[i])
                used[i] = True

                dfs(path)

                path.pop()
                used[i] = False

        dfs([])
        return result