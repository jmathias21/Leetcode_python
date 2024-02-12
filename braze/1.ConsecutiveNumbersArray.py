from typing import List
from collections import deque

class Solution:

    def replaceConsecutiveNumbers(self, mat):
        height = len(mat)
        width = len(mat[0])
        visited = set()

        def dfs(row, col, depth):
            if (row, col) in visited:
                return False

            if mat[row][col] == 0:
                return False
            
            meets_minimum = depth >= 3
            visited.add((row, col))
            for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if mat[new_row][new_col] != mat[row][col]:
                    continue

                meets_minimum = dfs(new_row, new_col, depth + 1) or meets_minimum

            if meets_minimum:
                mat[row][col] = 0
                return True
            return False
        
        for i in range(height):
            for j in range(width):
                dfs(i, j, 1)
                
        
solution = Solution()
answer = solution.replaceConsecutiveNumbers(
    [[1,3,5,6],
     [1,3,5,6],
     [1,2,2,6],
     [1,6,6,6]]
)
answer = solution.replaceConsecutiveNumbers(
    [[1,1,1,1],
     [1,1,1,2],
     [1,1,2,3],
     [1,6,5,4]]
)
answer = solution.replaceConsecutiveNumbers(
    [[1,3,5,6],
     [1,3,5,6],
     [1,2,2,6],
     [1,6,6,6]]
)
print(answer)

# Given a multi-dimensional array of numbers from 1-9, write a function that
# returns a multi-dimensional array where any consecutive numbers of at least
# length 3, get replaced with 0s. Numbers may be consecutive both horizontally
# or vertically.