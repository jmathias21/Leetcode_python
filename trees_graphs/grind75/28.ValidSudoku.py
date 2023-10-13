from collections import defaultdict
from typing import List

# https://leetcode.com/problems/valid-sudoku
# Tags: Hash map
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 27:00
    #
    # Use row, column, and sub-box dictionaries to store how many times we see each number in each
    # section. If we see the same number more than once in each section, it is not a valid sudoku
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_map = defaultdict(int)
        row_map = defaultdict(int)
        sub_map = defaultdict(int)

        for row in range(9):
            for col in range(9):
                number = board[row][col]

                if number != ".":
                    col_map[(col, number)] += 1
                    row_map[(row, number)] += 1

                    # Get the sub-box hash from our current row and col so that
                    # we have 9 sub-box keys
                    sub_box_hash = (row // 3) + ((col // 3) * 10)

                    sub_map[(sub_box_hash, number)] += 1

                    if col_map[(col, number)] > 1 or row_map[(row, number)] > 1 or sub_map[(sub_box_hash, number)] > 1:
                        return False
                    
        return True
        

solution = Solution()
answer = solution.isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)

answer = solution.isValidSudoku(
[[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]
)
print(answer)