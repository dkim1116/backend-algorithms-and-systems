class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        if len(nums) < 3: return result

        nums.sort()

        for start in range(len(nums) - 2):
            left = start + 1
            right = len(nums) - 1

            if start > 0 and nums[start] == nums[start - 1]: continue

            while left < right:
                total = nums[start] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[start], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
