# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class Solution:
    def isSubTree(self, root: TreeNode, subTree: TreeNode) -> bool:

        def isSameTree(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subTree: return True
        if not root: return False

        if isSameTree(root, subTree): return True

        return isSubTree(root.left, subTree) or isSubTree(root.right, subTree)