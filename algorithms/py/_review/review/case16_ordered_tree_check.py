from __future__ import annotations

# Ordered Tree Check
#
# Return True if the binary tree satisfies strict binary search tree ordering rules at every node.
# Otherwise return False.
#
# Input: root = [2, 1, 3]
# Output: True
# Input: root = [5, 1, 4, null, null, 3, 6]
# Output: False

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
    def solve(self, root: TreeNode | None) -> bool:
        pass
