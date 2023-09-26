from typing import List
from collections import deque

# https://leetcode.com/problems/rotting-oranges/
# Tags: BFS, Multisource BFS, Graph
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(n * m)
    # Time: Not timed
    #
    # The problem was solved using a multisource Breadth-First Search (BFS) initiated from
    # all rotten oranges, propagating the rot to their fresh neighbors, and tracking the
    # time (depth) taken to rot all oranges in the grid.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        max_depth = 0

        # find all rotten oranges and add them to BFS queue. Also
        # find the total amount of fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                if grid[row][col] == 1:
                    fresh_count += 1

        while queue:
            row, col, depth = queue.popleft()

            # find fresh oranges nearby, mark them as rotten, and add them to the
            # queue. Keep track of the max depth of our BFS so that we know how many
            # "minutes" have passed before there's no fresh oranges left
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = row + dx, col + dy

                if nx >= 0 and ny >= 0 and nx < rows and ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    max_depth = depth + 1
                    queue.append((nx, ny, depth + 1))

        # if there's still some fresh oranges left, we return -1
        if fresh_count > 0:
            return -1
            
        return max_depth

        
solution = Solution()
answer = solution.orangesRotting([[2,2],[1,1],[0,0],[2,0]])
answer = solution.orangesRotting([[1,2]])
answer = solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
answer = solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(answer)