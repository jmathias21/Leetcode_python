from typing import List

class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}

# https://leetcode.com/problems/word-search-ii/
# Tags: Prefix Tree, Trie, DFS, Backtracking
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = set()
        width = len(board[0])
        height = len(board)

        root = TrieNode()

        # build prefix tree
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_terminal = True

        def dfs(curr, node, row, col, depth):
            curr.append(board[row][col])
            
            if node.is_terminal:
                output.add("".join(curr))

            temp = board[row][col]
            board[row][col] = "#"
            for row_mod, col_mod in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_row, new_col = row_mod + row, col_mod + col

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if board[new_row][new_col] not in node.children:
                    continue

                dfs(curr, node.children[board[new_row][new_col]], new_row, new_col, depth + 1)
            curr.pop()
            board[row][col] = temp

        for i in range(height):
            for j in range(width):
                if board[i][j] in root.children:
                    dfs([], root.children[board[i][j]], i, j, 0)

        return output

        
solution = Solution()
answer = solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
print(answer)