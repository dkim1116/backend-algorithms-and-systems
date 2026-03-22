# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def dfs(node):
            if not node: return 0

            leftPath = dfs(node.left)
            rightPath = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, leftPath + rightPath)

            return 1 + max(leftPath, rightPath)

        dfs(root)
        return diameter