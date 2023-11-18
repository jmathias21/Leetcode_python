from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(mn)
    # Space Complexity: O(mn)
    # Time: 25:00
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        width = len(matrix[0])
        height = len(matrix)
        largest = 0

        for i in range(height):
            for j in range(width):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    largest = max(largest, 1)
                    min_depth = float('inf')
                    if i > 0 and j > 0:
                        min_depth = min(min_depth, matrix[i - 1][j])
                        min_depth = min(min_depth, matrix[i][j - 1])
                        min_depth = min(min_depth, matrix[i - 1][j - 1])
                        matrix[i][j] = min_depth + 1
                        largest = max(largest, matrix[i][j])

        return largest ** 2
        
solution = Solution()
answer = solution.maximalSquare(
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","1","1","1"]])
answer = solution.maximalSquare(
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]])
print(answer)