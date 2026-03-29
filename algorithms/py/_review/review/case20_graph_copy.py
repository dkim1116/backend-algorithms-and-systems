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
    def cloneGraph(self, node: Node | None) -> Node | None:
        pass
