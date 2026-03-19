# using used checks
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i] == True:
                    continue

                path.append(nums[i])
                used[i] = True

                dfs(path)

                path.pop()
                used[i] = False

        dfs([])
        return result

# using swap
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(index):
            if index == len(nums):
                result.append(nums[:])
                continue
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        dfs(0)
        return result