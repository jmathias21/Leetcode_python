from typing import List

# https://leetcode.com/problems/rotate-image/
# Tags: Rotate groups of 4 cells, matrix, matrix rotation
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 60:00
    #
    # The algorithm for rotating a cell 90-degrees is:
    # new_row = col
    # new_col = size - 1 - row
    #
    # We start with the outer-most layer, and rotate groups of 4 cells until we'e finished that layer.
    # Then we move one layer deeper and rotate those cells. We do this until the entire matrix has been
    # rotated
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)

        for origin in range(size // 2):
            for i in range(origin, size - origin - 1):
                row, col = origin, i
                prev = matrix[row][col]

                # rotate group of 4 cells
                for _ in range(4):
                    new_row, new_col = col, size - 1 - row
                    temp = matrix[new_row][new_col]
                    matrix[new_row][new_col] = prev
                    prev = temp
                    row, col = new_row, new_col
            
        
solution = Solution()
answer = solution.rotate(
    [[5,1,9,11],
     [2,4,8,10],
     [13,3,6,7],
     [15,14,12,16]]
)
answer = solution.rotate(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)
print(answer)