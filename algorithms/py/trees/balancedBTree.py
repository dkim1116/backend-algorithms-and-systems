class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node):
            if not node: return 0

            leftPath = dfs(node.left)
            if leftPath == -1: return -1
            rightPath = dfs(node.right)
            if rightPath == -1: return -1

            if abs(leftPath - rightPath) > 1: return -1

            return 1 + max(leftPath, rightPath)

        return False if dfs(root) == -1 else True