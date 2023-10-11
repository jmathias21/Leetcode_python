from typing import List

# https://leetcode.com/problems/word-search/
# Tags: Backtracking, Recursion, Graph, Matrix
class Solution:

    # Runtime Complexity: O(N * (3 ^ L)) where N is total cells, and L is the length of the word
    # Space Complexity: O(N)
    # Time: Not timed
    #
    # Look for the first character of the word throughout the entire board. When we find it, begin
    # a backtracking search for each next character while keeping track of the cells we've visited
    # in the current backtracking stack so we don't visit the same cell twice. If the word can't be
    # completed, we backtrack and try a different direction. If the word is found, we return True
    # up the stack
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board[0])
        height = len(board)
        visited = [[False] * width for _ in range(height)]
        first_char = word[0]

        def backtrack(i, row, col):
            if visited[row][col]:
                return False
            
            if i == len(word) - 1:
                return True
            
            visited[row][col] = True
            found_word = False

            for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rx, cx = row + row_offset, col + col_offset

                if rx >= 0 and rx < height and cx >= 0 and cx < width and board[rx][cx] == word[i + 1]:
                    found_word = found_word or backtrack(i + 1, rx, cx)
                    if found_word: break

            visited[row][col] = False
            return found_word

        for row in range(height):
            for col in range(width):
                if board[row][col] == first_char:
                    if backtrack(0, row, col):
                        return True
                    
        return False


        
solution = Solution()
answer = solution.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
answer = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
answer = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
print(answer)