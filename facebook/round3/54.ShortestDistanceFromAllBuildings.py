from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n^2 * m^2)
    # Space Complexity: O(n * m)
    # Time: 40:00
    def shortestDistance(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        total_houses = 0

        def bfs(row, col):
            visited = set()
            houses_visited = 0
            travel_distance = 0

            queue = deque([(row, col, 0)])

            while queue:
                row, col, depth = queue.popleft()

                if (row, col) in visited:
                    continue

                visited.add((row, col))

                if grid[row][col] == 1 and depth > 0:
                    houses_visited += 1
                    travel_distance += depth
                    continue

                for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_row, new_col = row + row_mod, col + col_mod

                    if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                        continue

                    if grid[new_row][new_col] == 2:
                        continue

                    queue.append((new_row, new_col, depth + 1))
            if travel_distance == 6:
                pass
            return travel_distance if houses_visited == total_houses else -1

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    total_houses += 1

        shortest_dist = float('inf')
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    continue

                travel_distance = bfs(i, j)
                if travel_distance != -1:
                    shortest_dist = min(shortest_dist, bfs(i, j))

        return shortest_dist if shortest_dist != float('inf') else -1

    
solution = Solution()
answer = solution.shortestDistance(
    [[1,0,2,0,1],
     [0,0,0,0,0],
     [0,0,1,0,0]]
)
print(answer)