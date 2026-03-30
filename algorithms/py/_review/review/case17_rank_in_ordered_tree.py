from __future__ import annotations

# Rank In Ordered Tree
#
# Given a binary search tree, return the k-th smallest value in sorted order.
#
# Input: root = [3, 1, 4, null, 2], k = 1
# Output: 1
# Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 3
# Output: 3

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
    def solve(self, root: TreeNode | None, k: int) -> int:
        count = 0
        res = None

        def dfs(node):
            nonlocal count, res

            if not node or res is not None:
                return None
            
            dfs(node.left)
            count += 1

            if count == k:
                res = node.val
            
            dfs(node.right)

        dfs(root)
        return res
