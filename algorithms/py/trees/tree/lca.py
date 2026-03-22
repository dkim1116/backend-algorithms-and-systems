class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if not node: return None

            if node == p or node == q: return node

            leftPath = dfs(node.left)
            rightPath = dfs(node.right)

            if leftPath and rightPath: return node

            return leftPath or rightPath

        return dfs(root)