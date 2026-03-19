const maximumPath = (root) => {
    let maxSum = -Infinity;

    const dfs = (node) => {
        if (!node) return 0;

        const leftSum = Math.max(0, dfs(node.left));
        const rightSum = Math.max(0, dfs(node.right));

        maxSum = Math.max(maxSum, leftSum + node.val + rightSum);

        return Math.max(leftSum + node.val, rightSum + node.val);
    }

    return maxSum === -Infinity ? 0 : maxSum;
}

// Restate: This looks like a problem where I can leverage postOrder depth first search.
// I need to compute the children at every subtree's root node first to find a total sum at every root node.
// My DFS helper function will check leftPathSum and rightPathSum and make sure it takes a bigger sum compared to 0
// to account for negatives.
// Every subtree's root node will check for total pathSum with its computed children and update the global best if needed
const maxPath = (root) => {
    let best = -Infinity;

    const dfs = (node) => {
        if (!node) return 0;

        const leftPathSum = Math.max(0, dfs(node.left));
        const rightPathSum = Math.max(0, dfs(node.right));

        best = Math.max(best, node.val + leftPathSum + rightPathSum);

        return Math.max(node.val + leftPathSum, node.val + rightPathSum);
    }

    dfs(root);
    return best;
}