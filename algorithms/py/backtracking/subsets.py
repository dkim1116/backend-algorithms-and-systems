class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(index, path):
            result.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])

        return result