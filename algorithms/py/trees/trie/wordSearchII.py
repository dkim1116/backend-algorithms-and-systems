# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


# Pattern:
#     Prefix Trie + DFS Backtracking

# Approach:
#     I build a prefix trie from all words so I can efficiently check whether the current path
#     on the board is still a valid prefix of any word.
#     
#     Then I run DFS from each cell in the board. At each step, I check whether the current
#     board character exists in the current trie node. If it does not, I stop exploring that path early.
#     If it does, I move to the next trie node and continue exploring in all four directions.
#     
#     If I reach a trie node containing "#", that means I found a complete word, so I add it to
#     the result and delete the marker to avoid duplicate results.
#     
#     During DFS, I mark the current board cell as visited with "*" so it is not reused in the
#     same path, then restore it after exploring all directions to backtrack correctly.


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        wordTrie = {}

        for word in words:
            node = wordTrie
            
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char] 
            node["#"] = word

        rows = len(board)
        cols = len(board[0])
        result = []
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(row, col, node):
            char = board[row][col]

            if char not in node:
                return

            nextNode = node[char]
            board[row][col] = "*"

            if "#" in nextNode:
                result.append(nextNode["#"])
                del nextNode["#"]

            for dirRow, dirCol in dirs:
                newRow = row + dirRow
                newCol = col + dirCol

                if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and board[newRow][newCol] != "*":
                    dfs(newRow, newCol, nextNode)

            board[row][col] = char        

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, wordTrie)

        return result