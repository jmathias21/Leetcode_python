from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(mn)
    # Space Complexity: O()
    # Time: started 6:28
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        width = len(matrix[0])
        height = len(matrix)
        max_size = 0

        for i in range(height):
            for j in range(width):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1

                    max_size = max(max_size, matrix[i][j])

        return max_size ** 2

        
solution = Solution()
answer = solution.maximalSquare(
    [["0","1"],
     ["1","0"]]
)
answer = solution.maximalSquare(
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","1","1","1"]]
)
print(answer)