# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# DFS solution
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        numIsland = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        rowL, colL = len(grid), len(grid[0])

        def dfs(startX, startY):
            if startX < 0 or startX >= rowL or startY < 0 or startY >= colL: return

            grid[startX][startY] = "0"

            for dirX, dirY in dirs:
                newX = startX + dirX
                newY = startY + dirY

                if newX < 0 or newX >= rowL or newY < 0 or newY >= colL: continue

                if grid[newX][newY] == "1":
                    dfs(newX, newY)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(x, y)
                    numIsland += 1

        return numIsland

# BFS solution
class Solution:
    def numIslandsBFS(self, grid: list[list[str]]) -> int:
        numIsland = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        rowL, colL = len(grid), len(grid[0])

        def bfs(startX, startY):
            queue = deque()
            queue.append([startX, startY])
            grid[startX][startY] = "0"

            while len(queue):
                row, col = queue.popleft()

                for dirX, dirY in dirs:
                    newX = row + dirX
                    newY = col + dirY

                    if newX < 0 or newX >= rowL or newY < 0 or newY >= colL: continue

                    if grid[newX][newY] == "1":
                        grid[newX][newY] = "0"
                        queue.append([newX, newY])

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    bfs(x,y)
                    numIsland += 1

        return numIsland

