from __future__ import annotations

# Tree Span
#
# The span of a binary tree is the number of edges in the longest path between any two nodes.
# Return that value.
#
# Input: root = [1, 2, 3, 4, 5]
# Output: 3
# Input: root = [1, 2]
# Output: 1

class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root: TreeNode | None) -> int:
        maxDiameter = 0

        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0
            
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)

            maxDiameter = max(maxDiameter, leftPath + rightPath)

            return 1 + max(leftPath, rightPath)
        dfs(root)
        return maxDiameter
