from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        max_depth = size // 2
        depth = 0
        while depth < max_depth:
            for i in range(depth, size - 1 - depth):
                row, col = depth, i
                prev = matrix[row][col]
                
                for _ in range(4):
                    prev_row = row
                    row = col
                    col = size - 1 - prev_row
                    new_prev = matrix[row][col]
                    matrix[row][col] = prev
                    prev = new_prev

            depth += 1


        
solution = Solution()
answer = solution.rotate(
    [[5,1,9,11],
     [2,4,8,10],
     [13,3,6,7],
     [15,14,12,16]])
print(answer)

# new_i = j
# new_j = N - 1 - i