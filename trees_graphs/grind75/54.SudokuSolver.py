from collections import defaultdict
from typing import List

# https://leetcode.com/problems/sudoku-solver/
# Tags: Backtracking
class Solution:

    # Runtime Complexity: O(1)
    # Space Complexity: O(1)
    # Time: Not timed
    def solveSudoku(self, board: List[List[str]]) -> None:
        size = 9
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)
        
        # find a valid number for a board position and make sure it's the same
        # or higher than the current num
        def getValidNum(row, col, num):
            for i in range(num, size + 1):
                if i not in row_map[row] and i not in col_map[col] and i not in box_map[(row // 3, col // 3)]:
                    return i
            return -1
            
        def backtrack(row, col):
            if row == size:
                return True
            if col == size:
                return backtrack(row + 1, 0)
            
            if board[row][col] == ".":
                num = 0
                while (num := getValidNum(row, col, num + 1)) != -1:
                    # fill in valid number
                    board[row][col] = str(num)
                    row_map[row].add(num)
                    col_map[col].add(num)
                    box_map[(row // 3, col // 3)].add(num)
                    
                    # move to the next position
                    if backtrack(row, col + 1):
                        return True
                    else:
                        # if the next position is invalid, remove the current number from
                        # the board so we can try a different one
                        row_map[row].remove(num)
                        col_map[col].remove(num)
                        box_map[(row // 3, col // 3)].remove(num)
                        board[row][col] = "."
                # no valid numbers found
                return False
            else:
                # We found a number that was already placed, so skip it
                return backtrack(row, col + 1)
        
        # prefill maps with initial game board
        for row in range(size):
            for col in range(size):
                num = board[row][col]
                if num != '.':
                    row_map[row].add(int(num))
                    col_map[col].add(int(num))
                    box_map[(row // 3, col // 3)].add(int(num))

        backtrack(0, 0)

                
        
solution = Solution()
answer = solution.solveSudoku(
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
)
print(answer)

    #  [["5","3","4","6","7","8","9","1","2"],
    #   ["6","7","2","1","9","5","3","4","8"],
    #   ["1","9","8","3","4","2","5","6","7"],
    #   ["8","5","9","7","6","1","4","2","3"],
    #   ["4","2","6","8","5","3","7","9","1"],
    #   ["7","1","3","9","2","4","8","5","6"],
    #   ["9","6","1","5","3","7","2","8","4"],
    #   ["2","8","7","4","1","9","6","3","5"],
    #   ["3","4","5","2","8","6","1","7","9"]]