# Description
# A grid contains empty cells, fresh items, and rotten items.
# Every minute, any fresh item directly adjacent up, down, left, or right to a rotten one also becomes rotten.
# Return the minimum minutes needed for all fresh items to rot, or -1 if it is impossible.
#
# Examples
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
#
# Constraints
# - Inputs follow the shapes shown in the examples.
# - Preserve the row and column boundaries described by the prompt.
# - Return exactly the value, collection, or boolean requested.
# - Assume the input size can be large enough that inefficient brute-force approaches may time out.
