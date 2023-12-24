from typing import List

# https://leetcode.com/problems/number-of-islands/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 10:00
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)

        def dfs(row, col):
            if grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            for r_mod, c_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_r, new_c = row + r_mod, col + c_mod

                if new_r < 0 or new_c < 0 or new_r >= height or new_c >= width:
                    continue

                if grid[new_r][new_c] == '0':
                    continue

                dfs(new_r, new_c)

        result = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == '1':
                    dfs(row, col)
                    result += 1

        return result

        
solution = Solution()
answer = solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(answer)