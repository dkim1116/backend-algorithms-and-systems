# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.


# Pattern:
#     DP

# Approach:
#     At any given point in the grid, the only path to the top left is row - 1 or col - 1
#     I create a grid of minimum possible sum at every possible position by looking at top and left element at any given position
#     I sum up every possible path then return the bottom right of the grid I created with sums

# Time & Space Complexity:
#     Time complexity is O(r * c) as we need to iterate through every cell in the matrix to compute the minimum path sum
#     Space complexity is O(r * c) as we need to create a grid with sums

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    grid[row][col] = grid[row][col]
                elif row == 0:
                    grid[row][col] = grid[row][col] + grid[row][col - 1]
                elif col == 0:
                    grid[row][col] = grid[row][col] + grid[row - 1][col]
                else:
                    grid[row][col] = grid[row][col] + min(
                        grid[row - 1][col],
                        grid[row][col - 1]
                    )

        return grid[rows - 1][cols - 1]
