from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 18:00
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board[0])
        height = len(board)
        seen = set()
        word_exists = False

        def dfs(row, col, i):
            if i == len(word) - 1:
                return True

            seen.add((row, col))
            for row_mod, col_mod in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if (new_row, new_col) in seen:
                    continue

                if word[i + 1] != board[new_row][new_col]:
                    continue

                nonlocal word_exists
                word_exists = word_exists or dfs(new_row, new_col, i + 1)

            seen.remove((row, col))

            return word_exists
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False


        
solution = Solution()
answer = solution.exist(
    [["A","B","C","E"],
     ["S","F","C","S"],
     ["A","D","E","E"]], "SEE")

answer = solution.exist(
    [["A","B","C","E"],
     ["S","F","C","S"],
     ["A","D","E","E"]], "ABCCED")
print(answer)