from typing import List
from collections import defaultdict

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(n * m)
    # Time: 18:00
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        width = len(grid[0])
        height = len(grid)

        def dfs(island, row, col):
            visited.add((row, col))
            for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if (new_row, new_col) in visited:
                    continue

                if grid[new_row][new_col] != '1':
                    continue

                dfs(island, new_row, new_col)

        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(count, i, j)
                    count += 1

        return count

        
solution = Solution()
answer = solution.numIslands(
    [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
)
print(answer)