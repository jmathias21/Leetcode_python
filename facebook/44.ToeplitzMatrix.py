from typing import List

# https://leetcode.com/problems/toeplitz-matrix/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 13:00
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        h = len(matrix)
        w = len(matrix[0])

        def check_diagonal(row, col):
            val = matrix[row][col]
            for i in range(1, h):
                new_col, new_row = col + i, row + i
                if new_col >= w or new_row >= h:
                    break
                if matrix[new_row][new_col] != val:
                    return False
            return True

        for col in range(w - 1):
            if not check_diagonal(0, col):
                return False
                
        for row in range(1, h - 1):
            if not check_diagonal(row, 0):
                return False
            
        return True
            
        
solution = Solution()
answer = solution.isToeplitzMatrix(
    [[1,2,3,4],
     [5,1,2,3],
     [9,5,1,2]]
)
print(answer)