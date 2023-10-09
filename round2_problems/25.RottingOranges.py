from typing import List
from collections import deque

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 37:00
    def orangesRotting(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        queue = deque()
        visited = set()
        max_depth = 0
        oranges_rotted = 0
        total_oranges = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                if grid[i][j] == 1 or grid[i][j] == 2:
                    total_oranges += 1

        while queue:
            (i, j, depth) = queue.popleft()

            oranges_rotted += 1

            grid[i][j] = 2
            max_depth = max(max_depth, depth)
            
            if i > 0 and grid[i - 1][j] == 1 and (i - 1, j) not in visited:
                queue.append((i - 1, j, depth + 1))
                visited.add((i - 1, j))
            if i < height - 1 and grid[i + 1][j] == 1 and (i + 1, j) not in visited:
                queue.append((i + 1, j, depth + 1))
                visited.add((i + 1, j))
            if j > 0 and grid[i][j - 1] == 1 and (i, j - 1) not in visited:
                queue.append((i, j - 1, depth + 1))
                visited.add((i, j - 1))
            if j < width - 1 and grid[i][j + 1] == 1 and (i, j + 1) not in visited:
                queue.append((i, j + 1, depth + 1))
                visited.add((i, j + 1))

        return max_depth if oranges_rotted == total_oranges else -1

        
solution = Solution()
# [[1,2,1,1,2,1,1]]
#answer = solution.orangesRotting([[1,2,1,1,2,1,1]])
# [[2,1,1],[1,1,0],[0,1,1]]
answer = solution.orangesRotting([
    [2,1,1],
    [1,1,0],
    [0,1,1]
])
print(answer)