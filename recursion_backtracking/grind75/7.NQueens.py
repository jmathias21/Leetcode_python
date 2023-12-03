from typing import List

# https://leetcode.com/problems/n-queens/
# Tags: Backtracking
class Solution:

    # Runtime Complexity: O(n!)
    # Space Complexity: O(n)
    # Time: Not timed
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        visited_cols = set()
        visited_diags = set()
        visited_antidiags = set()

        def canPlace(row, col):
            if col in visited_cols:
                return False
            if row - col in visited_diags:
                return False
            if row + col in visited_antidiags:
                return False
            return True
        
        def backtrack(row):
            if row == n:
                output.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if canPlace(row, col):
                    board[row][col] = 'Q'
                    visited_cols.add(col)
                    visited_diags.add(row - col)
                    visited_antidiags.add(row + col)

                    backtrack(row + 1)

                    board[row][col] = '.'
                    visited_cols.remove(col)
                    visited_diags.remove(row - col)
                    visited_antidiags.remove(row + col)

        backtrack(0)
        return output

        
solution = Solution()
answer = solution.solveNQueens(4)
print(answer)