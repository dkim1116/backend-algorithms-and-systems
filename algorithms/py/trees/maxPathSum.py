# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float(-inf)

        def dfs(node):
            nonlocal maxSum
            if not node: return 0

            leftPathSum = max(0, dfs(node.left))
            rightPathSum = max(0, dfs(node.right))

            maxSum = max(maxSum, node.val + leftPathSum + rightPathSum)

            return node.val + max(leftPathSum, rightPathSum)

        dfs(root)
        return maxSum