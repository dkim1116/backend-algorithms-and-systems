const getDiameter = (root) => {
    let best = -Infinity;

    const postOrderDFS = (node) => {
        if (!node) return 0;

        const leftHeight = postOrderDFS(node.left);
        const rightHeight = postOrderDFS(node.right);

        best = Math.max(best, leftHeight + rightHeight);

        return 1 + Math.max(leftHeight, rightHeight);
    }
    postOrderDFS(root);
    return best === -Infinity ? 0 : best;
};

const getDiameter2 = (root) => {
    let best = 0;

    const dfs = (node) => {
        if (!node) return 0;

        const leftHeight = dfs(node.left);
        const rightHeight = dfs(node.right);

        best = Math.max(best, leftHeight + rightHeight);

        return 1 + Math.max(leftHeight, rightHeight);
    }

    dfs(root);
    return best;
}