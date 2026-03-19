

// /**
//  * LeetCode: Number of Islands
//  *
//  * Given an m x n 2D binary grid `grid` which represents a map of '1's (land)
//  * and '0's (water), return the number of islands.
//  *
//  * An island is surrounded by water and is formed by connecting adjacent lands
//  * horizontally or vertically. You may assume all four edges of the grid are
//  * all surrounded by water.
//  *
//  * Example 1:
//  * Input: grid = [
//  *   ['1','1','1','1','0'],
//  *   ['1','1','0','1','0'],
//  *   ['1','1','0','0','0'],
//  *   ['0','0','0','0','0']
//  * ]
//  * Output: 1
//  *
//  * Example 2:
//  * Input: grid = [
//  *   ['1','1','0','0','0'],
//  *   ['1','1','0','0','0'],
//  *   ['0','0','1','0','0'],
//  *   ['0','0','0','1','1']
//  * ]
//  * Output: 3
//  *
//  * Constraints:
//  * - m == grid.length
//  * - n == grid[i].length
//  * - 1 <= m, n <= 300
//  * - grid[i][j] is '0' or '1'
//  *
//  * Notes:
//  * - Adjacent means up, down, left, right (no diagonals)
//  * - You should modify the grid or use a visited structure to avoid revisiting
//  */

// const numberOfIslands = (grid) => {
//     const visited = new Set();
//     const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
//     let islandCount = 0;

//     const bfs = (startX, startY) => {
//         const queue = [[startX, startY]];
//         let head = 0;

//         while (head < queue.length) {
//             const [x, y] = queue[head++];
//             for (let [dx, dy] of directions) {
//                 const nx = x + dx;
//                 const ny = y + dy;
//                 const newCoords = nx + ',' + ny;

//                 if (nx < 0 || nx >= grid.length) continue;
//                 if (ny < 0 || ny >= grid[0].length) continue;
//                 if (visited.has(newCoords)) continue;
//                 if (grid[nx][ny] === '0') continue;

//                 visited.add(newCoords);
//                 queue.push([nx, ny]);
//             }
//         }
//     }

//     for (let x = 0; x < grid.length; x++) {
//         for (let y = 0; y < grid[0].length; y++) {
//             const coords = x + ',' + y;
//             if (visited.has(coords)) continue;
//             if (grid[x][y] === '0') continue;

//             visited.add(coords);
//             islandCount++;
//             bfs(x, y);
//         }
//     }

//     return islandCount;
// };

const numberOfIslands = (grid) => {
    if (grid.length === 0) return 0;

    const visited = new Set();
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let numberOfIslands = 0;

    const xLength = grid.length;
    const yLength = grid[0].length;

    const bfs = (startX, startY) => {
        const queue = [[startX, startY]];
        let head = 0;

        while (head < queue.length) {
            const [x, y] = queue[head++];

            for (let [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                const coords = nx + ',' + ny;

                if (nx < 0 || nx >= xLength) continue;
                if (ny < 0 || ny >= yLength) continue;
                if (visited.has(coords)) continue;
                if (grid[nx][ny] === '0') continue;

                visited.add(coords);
                queue.push([nx, ny]);
            }
        }
    }

    for (let x = 0; x < xLength; x++) {
        for (let y = 0; y < yLength; y++) {
            const coords = x + ',' + y;

            if (visited.has(coords)) continue;
            if (grid[x][y] === '0') continue;

            visited.add(coords);
            numberOfIslands++;
            bfs(x, y);
        }
    }

    return numberOfIslands;
};

const numOfIslands = (grid) => {
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    let islandCount = 0;
    let xLength = grid.length;
    let yLength = grid[0].length;

    const dfs = (startX, startY) => {
        if (startX < 0 || startX >= xLength || startY < 0 || startY >= yLength) return;

        grid[startX][startY] = "0";

        for (let [dirX, dirY] of dirs) {
            const newX = startX + dirX;
            const newY = startY + dirY;

            if (newX < 0 || newX >= xLength) continue;
            if (newy < 0 || newY >= yLength) continue;
            
            if (grid[newX][newY] === "1") {
                dfs(newX, newY);
            }
        }
    }

    for (let x = 0; x < xLength; x++) {
        for (let y = 0; y < yLength; y++) {
            if (grid[x][y] === "1") {
                dfs(x, y);
                islandCount++;
            }
        }
    }

    return islandCount;
}