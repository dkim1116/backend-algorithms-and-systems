# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Pattern:
#     BFS Tree traversal

# Approach:
#     I traverse the tree from root using BFS to go level by level
#     I keep track of which column each node is on and create a mapping of it while keeping track of furthest left and right column
#     I iterate the range from [farLeft, farRight] then add to result

# Time & Space complexity:
#     Time complexity is O(n) as I need to traverse every single node in the tree once
#     Space complexity is O(n) as the space grows linearly for result, queue, and hashmap depending on the size of the tree

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: 
            return []
        
        farLeft = 0
        farRight = 0

        columnMapping = {}

        queue = [[root, 0]]
        queuePointer = 0

        while queuePointer < len(queue):
            node, col = queue[queuePointer]
            queuePointer += 1

            columnMapping[col] = columnMapping.get(col, [])
            columnMapping[col].append(node.val)

            farLeft = min(farLeft, col)
            farRight = max(farRight, col)

            if node.left:
                queue.append([node.left, col - 1])

            if node.right:
                queue.append([node.right, col + 1])

        result = []

        for col in range(farLeft, farRight + 1):
            result.append(columnMapping.get(col, []))

        return result