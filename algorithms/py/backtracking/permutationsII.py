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

# Swap check
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        def dfs(index):
            if index == len(nums):
                result.append(nums[:])
                return

            seen = set()

            for i in range(index, len(nums)):
                if nums[i] in seen:
                    continue

                seen.add(nums[i])

                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        dfs(0)
        return result