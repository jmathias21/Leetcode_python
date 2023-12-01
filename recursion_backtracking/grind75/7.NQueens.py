from typing import List

# https://leetcode.com/problems/n-queens/
# Tags: Backtracking
class Solution:

    # Runtime Complexity: O(n!)
    # Space Complexity: O(n)
    # Time: Not timed
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)] # start with empty board
        res=[]
        
        visited_cols=set()
        visited_diagonals=set()
        visited_antidiagonals=set()

        def canPlace(row, col):
            if col in visited_cols:
                return False
            if row - col in visited_diagonals:
                return False
            if row + col in visited_antidiagonals:
                return False
            return True
        
        def backtrack(row):
            if row == n:                
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                # If the current square doesn't have another queen in same column and diagonal.
                if canPlace(row, col):
                    board[row][col]='Q' # place the queen
                    visited_cols.add(col)
                    visited_diagonals.add(row - col)
                    visited_antidiagonals.add(row + col)
                    backtrack(row + 1) 

                    # reset the path
                    board[row][col]='.'
                    visited_cols.remove(col)
                    visited_diagonals.remove(row - col)
                    visited_antidiagonals.remove(row + col)                       

        backtrack(0)
        return res

        
solution = Solution()
answer = solution.solveNQueens(4)
print(answer)