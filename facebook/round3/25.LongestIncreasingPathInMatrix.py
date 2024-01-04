from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O()
    # Time: started 7:32
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        width = len(matrix[0])
        height = len(matrix)
        memo = [[None for _ in range(width)] for _ in range(height)]
        longest = 0

        def dfs(row, col):
            if memo[row][col]:
                return memo[row][col]

            max_depth = 1
            for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if matrix[new_row][new_col] <= matrix[row][col]:
                    continue

                max_depth = max(max_depth, dfs(new_row, new_col) + 1)

            memo[row][col] = max_depth
            return max_depth
        
        for row in range(height):
            for col in range(width):
                longest = max(longest, dfs(row, col))

        return longest
            
        
solution = Solution()
answer = solution.longestIncreasingPath(
    [[9,9,4],
     [6,6,8],
     [2,1,1]]
)
print(answer)