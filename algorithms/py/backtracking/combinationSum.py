class Solution:
    def combinationSum(self, nums: list[int], target) -> list[list[int]]:
        result = []

        def dfs(index, path, sum):
            if sum == target:
                result.append(path[:])
                return

            if sum > target:
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i, path, sum + nums[i])
                path.pop()

        dfs(0, [], 0)
        return result