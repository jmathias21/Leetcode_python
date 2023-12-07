from typing import List
from collections import deque

# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Tags: BFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 16:00
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        height = len(grid)
        width = len(grid[0])
        queue = deque([(0, 0, 0)])

        while queue:
            row, col, depth = queue.popleft()

            if row == height - 1 and col == width - 1:
                return depth + 1
            
            if grid[row][col] == 1:
                continue

            grid[row][col] = 1
            for row_mod, col_mod in [(-1,-1),(1,1),(-1,1),(1,-1),(1,0),(0,1),(-1,0),(0,-1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if grid[new_row][new_col] != 0:
                    continue

                queue.append((new_row, new_col, depth + 1))

        return -1

        
solution = Solution()
answer = solution.shortestPathBinaryMatrix(
    [[0,0,0],
     [1,1,0],
     [1,1,0]])
print(answer)