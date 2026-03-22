# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []

        result = []
        queue = [root]
        queuePointer = 0

        while queuePointer < len(queue):
            levelSize = len(queue) - queuePointer
            level = []
            
            for i in range(levelSize):
                currNode = queue[queuePointer]
                queuePointer += 1
                level.append(currNode.val)

                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)

            result.append(level)

        return result

        