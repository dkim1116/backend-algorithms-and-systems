# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Range boundary
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minimum, maximum):
            if not node: return True
            if minimum is not None and node.val <= minimum: return False
            if maximum is not None and node.val >= maximum: return False

            return dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum)
        
        return dfs(root, None, None)
        
# Inorder traversal
class Solution:
    def isValidBSTInorder(self, root: TreeNode) -> bool:
        stack = []
        left = root
        prev = None

        while len(stack) or left:
            while left:
                stack.append(left)
                left = left.left

            node = stack.pop()
            if prev is not None and prev >= node.val:
                return False
            prev = node.val
            left = left.right

        return True