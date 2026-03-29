from __future__ import annotations

# Graph Copy
#
# You are given a reference to a node in a connected undirected graph.
# Return a deep copy of the entire graph.
#
# Input: adjacency = [[2, 4], [1, 3], [2, 4], [1, 3]]
# Output: a deep-copied graph with the same structure
# Input: adjacency = [[]]
# Output: a single copied node

class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def solve(self, node: Node | None) -> Node | None:
        if not node:
            return None
        cloneMap = {}

        def dfs(currNode):
            if currNode in cloneMap:
                return cloneMap[currNode]
            
            clone = Node(currNode.val)
            cloneMap[currNode] = clone

            for neighbor in currNode.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        
        return dfs(node)
