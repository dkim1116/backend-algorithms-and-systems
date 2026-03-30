from __future__ import annotations

# Shared Ancestor
#
# Given the root of a binary tree and two nodes p and q that both exist in the tree, return their lowest common ancestor.
#
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# Output: 3
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
# Output: 5

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
    def solve(
        self,
        root: TreeNode | None,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode | None:
        
        def dfs(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)

            if leftPath and rightPath:
                return node
            
            return leftPath or rightPath
        return dfs(root)
