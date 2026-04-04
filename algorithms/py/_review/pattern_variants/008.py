# Description
# A sequence of undirected edges is added one by one to a graph whose nodes are labeled from 1 to n.
# Exactly one added edge creates a cycle in what was otherwise a tree-like structure.
# Return the edge that can be removed so the remaining edges form a valid tree again.
# If multiple answers are possible, return the one that appears last in the input.
#
# Examples
# Input: edges = [[1, 2], [1, 3], [2, 3]]
# Output: [2, 3]
# Input: edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
# Output: [1, 4]
#
# Constraints
# - 3 <= len(edges) <= 1000
# - Each edge has length 2.
# - 1 <= u, v <= len(edges)
# - The graph is connected after all edges are added.
