# Description
# Design two functions for a binary tree:
# one that converts the tree into a string representation, and one that rebuilds the same tree from that representation.
# Your format may be any deterministic format that preserves the exact structure and values.
#
# Examples
# Input: root = [1, 2, 3, null, null, 4, 5]
# Output: deserializing the serialized form reconstructs the same tree
# Input: root = []
# Output: deserializing the serialized form reconstructs the same empty tree
#
# Constraints
# - 0 <= number of nodes <= 10^4
# - -1000 <= node.val <= 1000
# - Preserve exact structure, not just values.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque;

class Solution:
    def deserializeTree(self, input: list[int]) -> TreeNode:
        if len(input) == 0:
            return None
        
        root = TreeNode(input[0])
        queue = deque([root])
        i = 1

        while queue and i < len(input):
            currNode = queue.popleft()

            if i < len(input) and input[i] is not None:
                currNode.left = TreeNode(input[i])
                queue.append(currNode.left)
            i += 1

            if i < len(input) and input[i] is not None:
                currNode.right = TreeNode(input[i])
                queue.append(currNode.right)
            i += 1

        return root