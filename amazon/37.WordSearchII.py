from typing import List

class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.word = ""
        self.children = {}

# https://leetcode.com/problems/word-search-ii/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:02
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        w = len(board[0])
        h = len(board)

        prefix_tree = TrieNode()

        for word in words:
            node = prefix_tree
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_terminal = True
            node.word = word

        visited = [[False for _ in range(w)] for _ in range(h)]
        output = set()

        def dfs(row, col, node, i):
            if visited[row][col]:
                return

            if node.is_terminal:
                output.add(node.word)
            
            visited[row][col] = True
            for r_mod, c_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                r, c = row + r_mod, col + c_mod

                if r < 0 or c < 0 or r >= h or c >= w:
                    continue

                if board[r][c] not in node.children:
                    continue

                prev = node
                node = node.children[board[r][c]]
                dfs(r, c, node, i + 1)
                node = prev
            visited[row][col] = False

        for row in range(h):
            for col in range(w):
                if board[row][col] in prefix_tree.children:
                    dfs(row, col, prefix_tree.children[board[row][col]], 0)

        return output
        
solution = Solution()
answer = solution.findWords(board = 
                            [["o","a","a","n"],
                             ["e","t","a","e"],
                             ["i","h","k","r"],
                             ["i","f","l","v"]], words = ["oath","pea","eat","rain"])
print(answer)


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]