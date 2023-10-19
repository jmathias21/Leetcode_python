from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 14:00
    def orangesRotting(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        queue = deque()
        max_depth = 0
        fresh_oranges = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    grid[row][col] = 1
                    fresh_oranges += 1
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        while queue:
            row, col, depth = queue.popleft()

            if grid[row][col] == 2:
                continue

            fresh_oranges -= 1
            max_depth = max(max_depth, depth)

            grid[row][col] = 2

            for row_mod, col_mod in [(-1, 0),(1,0),(0,-1),(0,1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if grid[new_row][new_col] != 1:
                    continue

                queue.append((new_row, new_col, depth + 1))

        return max_depth if fresh_oranges == 0 else -1
    
        
solution = Solution()
answer = solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(answer)