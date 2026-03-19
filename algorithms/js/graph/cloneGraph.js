const cloneGraph = (node) => {
    if (!node) return null;

    const map = new Map();

    const dfs = (currNode) => {
        if (map.has(currNode)) return map.get(currNode);

        const clone = { val: currNode.val, neighbors: [] };
        map.set(currNode, clone);

        for (let neighbor of currNode.neighbors) {
            clone.neighbors.push(dfs(neighbor));
        }

        return clone;
    }

    return dfs(node);
}

const cloneGraph2 = (node) => {
    if (!node) return null;

    const cloneMap = new Map();

    const dfs = (currNode) => {
        if (cloneMap.has(currNode)) return cloneMap.get(currNode);

        const clone = {val: currNode.val, neighbors: []};

        cloneMap.set(currNode, clone);

        for (let neighbor of currNode.neighbors) {
            clone.neighbors.push(dfs(neighbor))
        }

        return clone;
    }

    return dfs(currNode);
}