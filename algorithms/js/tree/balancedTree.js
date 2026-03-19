// Restate: Check if every subtree in a tree has a height difference of <= 1 in left subtree and right
// Pattern: I need to compute the children nodes in every subtree, so post-order DFS
// Invariant: Compute height of every subtree and exit if an unbalanced subtrees are found. If not, continue
// Action:
// - Find height of left subtree
// - Find height of right subtree
// If at any subtree is unbalanced, return -1 and exit out
// if the helper function returns -1, return false, else true
const isBalanced = (root) => {

    const getHeight = (node) => {

        if (!node) return 0;

        const leftHeight = getHeight(node.left);
        if (leftHeight === -1) return -1;

        const rightHeight = getHeight(node.right);
        if (rightHeight === -1) return -1;

        if (Math.abs(leftHeight - rightHeight) > 1) return -1;

        return 1 + Math.max(leftHeight, rightHeight);
    };

    return getHeight(root) !== -1 ? true : false;
};

const isBalanced2 = (root) => {

    const dfs = (node) => {
        if (!node) return 0;

        const leftHeight = dfs(node.left);
        if (leftHeight === -1) return -1;
        const rightHeight = dfs(node.right);
        if (rightHeight === -1) return -1;

        if (Math.abs(leftHeight - rightHeight) > 1) return -1;

        return 1 + Math.max(leftHeight, rightHeight);
    }

    return dfs(root) === -1 ? false : true;
};