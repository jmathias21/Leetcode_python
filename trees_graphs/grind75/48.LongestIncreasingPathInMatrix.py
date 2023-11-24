from typing import List

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Tags: DFS, Top-down dynamic programming
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Time: started 12:36, paused 12:54, started 1:00
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        width, height = len(matrix[0]), len(matrix)
        depths = [[0 for _ in range(width)] for _ in range(height)]
        
        def dfs(row, col):
            if depths[row][col] != 0:
                return depths[row][col]

            max_size = 1
            for row_mod, col_mod in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if matrix[new_row][new_col] <= matrix[row][col]:
                    continue

                max_size = max(max_size, dfs(new_row, new_col) + 1)

            depths[row][col] = max_size
            return max_size
        
        return max(dfs(r,c) for r in range(height) for c in range(width)) 

        
solution = Solution()
answer = solution.longestIncreasingPath(
    [[3,4,5],
     [3,2,6],
     [2,2,1]]
)
answer = solution.longestIncreasingPath2(
    [[9,9,4],
     [6,6,8],
     [2,1,1]]
)
print(answer)