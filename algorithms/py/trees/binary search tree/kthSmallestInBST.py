# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Pattern:
#     Tree traversal (inorder)

# Approach:
#     I need to find the kth smallest value in a BST. Binary tree is structured in a way where leftChild of node is smaller than node and rightChild of node is bigger than node
#     I will traverse inorder to go left -> root -> right and exit when we have reached kth node

# Time & Space complexity:
#     Time complexity is O(n)
#     Space complexity is O(h) where h is the height of the recursive stack

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Standard DFS
class SolutionDFS:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        result = None

        def dfs(node):
            nonlocal count, result

            if not node or result is not None:
                return
            
            dfs(node.left)
            count += 1

            if count == k:
                result = node.val

            dfs(node.right)

        dfs(root)
        return result
    
# Iterative
class SolutionItr:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        left = root
        count = 0

        while stack or left:
            while left:
                stack.append(left)
                left = left.left

            node = stack.pop()
            count += 1

            if count == k:
                return node.val

            left = node.right
