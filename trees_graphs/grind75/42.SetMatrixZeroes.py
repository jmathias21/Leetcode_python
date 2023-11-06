from typing import List

# https://leetcode.com/problems/set-matrix-zeroes/
# Tags: matrix
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(n * m)
    # Time: 13:00
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])
        rows_marked = set()
        cols_marked = set()

        for i in range(height):
            for j in range(width):
                if matrix[i][j] != 0:
                    continue

                if i not in rows_marked:
                    rows_marked.add(i)

                if j not in cols_marked:
                    cols_marked.add(j)

        while rows_marked:
            row = rows_marked.pop()
            for i in range(width):
                matrix[row][i] = 0

        while cols_marked:
            col = cols_marked.pop()
            for i in range(height):
                matrix[i][col] = 0