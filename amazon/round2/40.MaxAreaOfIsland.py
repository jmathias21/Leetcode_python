from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        curr_area = 0

        def dfs(row, col):
            if grid[row][col] == 0:
                return
            
            nonlocal curr_area
            curr_area += 1

            grid[row][col] = 0
            for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if grid[new_row][new_col] == 0:
                    continue

                dfs(new_row, new_col)

        max_area = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    curr_area = 0
                    dfs(i, j)
                    max_area = max(max_area, curr_area)

        return max_area
    
solution = Solution()
answer = solution.maxAreaOfIsland(
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
)
print(answer)