// Restate: find the maximum depth in a tree
// Pattern: I need to compute children first to get the length of each subtree. So post-order DFS.
// Invariant: Recursive calls return depth of subtrees.
// Action: starting from depth of 1, every time we dive into a child node, increase level + 1.
// Every time we get the length of subtrees, take the longer one.
// Why: This works because DFS tries to reach every leaf nodes first. We get each subtrees length
// and take the longer one.
const maxDepth = (root) => {
    if (!root) return 0;

    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

const maxDepth2 = (root) => {
    if (!root) return 0;

    return 1 + Math.max(maxDepth2(root.left), maxDepth2(root.right));
}