from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(n * m)
    # Time: started 6:12
    def largestIsland(self, grid: List[List[int]]) -> int:
        # find all islands
        # use size grid to store the size of the island on the island itself
        # loop through entire grid and get the max of all adjacent elements
        width = len(grid[0])
        height = len(grid)
        island_map = [[0 for _ in range(width)] for _ in range(height)]
        sizes = defaultdict(int)

        def dfs(row, col, hash):
            if grid[row][col] == 0:
                return

            sizes[hash] += 1
            island_map[row][col] = hash
            
            grid[row][col] = 0
            for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if grid[new_row][new_col] == 0:
                    continue

                dfs(new_row, new_col, hash)
        
        for row in range(height):
            for col in range(width):
                dfs(row, col, len(sizes) + 1)

        largest = sizes[1]
        for row in range(height):
            for col in range(width):
                if island_map[row][col] == 0:
                    size = 0
                    visited = set()
                    for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                        new_row, new_col = row + row_mod, col + col_mod

                        if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                            continue

                        if island_map[new_row][new_col] in visited:
                            continue

                        visited.add(island_map[new_row][new_col])
                        size += sizes[island_map[new_row][new_col]]

                    largest = max(largest, size + 1)

        return largest      

        
solution = Solution()
answer = solution.largestIsland(
    [[1,1],
     [1,1]]
)
answer = solution.largestIsland(
    [[1,0,1],
     [1,0,0],
     [0,1,1]]
)
print(answer)