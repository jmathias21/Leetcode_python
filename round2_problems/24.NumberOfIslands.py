from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Time: 20:00
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        visited = set()
        total_islands = 0

        def dfs(row, col):
            if row == 2 and col == 1:
                donothing = 0

            if (row, col) in visited:
                return
            
            visited.add((row, col))
            
            if row > 0 and grid[row - 1][col] == '1':
                dfs(row - 1, col)
            if row < height - 1 and grid[row + 1][col] == '1':
                dfs(row + 1, col)
            if col > 0 and grid[row][col - 1] == '1':
                dfs(row, col - 1)
            if col < width - 1 and grid[row][col + 1] == '1':
                dfs(row, col + 1)

        for i in range(height):
            for j in range(width):
                if (i, j) not in visited and grid[i][j] == '1':
                    total_islands += 1
                    dfs(i, j)

        return total_islands

        
solution = Solution()
answer = solution.numIslands(
[["1","1","1"],
 ["0","1","0"],
 ["1","1","1"]]) # 1
# answer = solution.numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]) # 3
print(answer)