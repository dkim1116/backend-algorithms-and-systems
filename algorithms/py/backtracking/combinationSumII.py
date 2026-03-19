class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        nums.sort()

        def dfs(index, path, sum):
            if sum == target:
                result.append(path[:])
                return

            if sum > target:
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                dfs(i + 1, path, sum + nums[i])
                path.pop()

        dfs(0,[],0)
        return result
