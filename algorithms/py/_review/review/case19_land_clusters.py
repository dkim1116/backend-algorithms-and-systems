from __future__ import annotations

# Land Clusters
#
# A grid contains '1' for land and '0' for water.
# Count how many disconnected land masses exist using 4-directional adjacency.
#
# Input: grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
# Output: 1
# Input: grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
# Output: 3

class Solution:
    def solve(self, grid: list[list[str]]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        land = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            grid[row][col] = '0'

            for dirX, dirY in dirs:
                newX = row + dirX
                newY = col + dirY

                if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == "1":
                    dfs(newX, newY)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    land += 1
                    dfs(row, col)

        return land
