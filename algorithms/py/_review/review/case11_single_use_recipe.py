from __future__ import annotations

# Single Use Recipe
#
# You are given ingredient values that may contain duplicates and a target total.
# Return all unique combinations that sum to target.
# Each array element may be used at most once.
#
# Input: values = [10, 1, 2, 7, 6, 1, 5], target = 8
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
# Input: values = [2, 5, 2, 1, 2], target = 5
# Output: [[1, 2, 2], [5]]

class Solution:
    def solve(self, values: list[int], target: int) -> list[list[int]]:
        values.sort()
        result = []

        def dfs(index, path, total):
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return
            
            for i in range(index, len(values)):
                if i > index and values[i] == values[i - 1]: continue

                path.append(values[i])
                dfs(i + 1, path, total + values[i])
                path.pop()
        dfs(0,[],0)
        return result
