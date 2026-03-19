const numOfProvinces = (grid) => {
    if (grid.length === 0) return 0;

    let numberOfProvinces = 0;

    const visited = new Set();

    const dfs = (city) => {
        for (let neighbor = 0; neighbor < grid.length; neighbor++) {
            if (grid[city][neighbor] === 1 && !visited.has(neighbor)) {
                visited.add(neighbor);
                dfs(neighbor);
            }
        }
    }

    for (let city = 0; city < grid.length; city++) {
        if (!visited.has(city)) {
            visited.add(city);
            numberOfProvinces++;
            dfs(city);
        }
    }

    return numberOfProvinces;
}