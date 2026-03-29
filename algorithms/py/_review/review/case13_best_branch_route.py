from __future__ import annotations

# Best Branch Route
#
# A path in a binary tree may start and end at any nodes, but it must move through parent-child connections.
# Return the maximum possible path sum.
#
# Input: root = [1, 2, 3]
# Output: 6
# Input: root = [-10, 9, 20, null, null, 15, 7]
# Output: 42

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
    def maxPathSum(self, root: TreeNode | None) -> int:
        pass
