from collections import deque
from typing import List

# https://leetcode.com/problems/rotting-oranges/
# Tags: 
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Time: 24:00
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        queue = deque()
        total_rotten = 0
        total_oranges = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] != 0:
                    total_oranges += 1
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        seen = set()
        while queue:
            row, col, depth = queue.popleft()

            if (row, col) in seen:
                continue

            total_rotten += 1
            if total_rotten == total_oranges:
                return depth

            seen.add((row, col))
            for r_mod, c_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_r, new_c = row + r_mod, col + c_mod

                if new_r < 0 or new_c < 0 or new_r >= height or new_c >= width:
                    continue

                if grid[new_r][new_c] != 1:
                    continue

                queue.append((new_r, new_c, depth + 1))

        return -1 if total_oranges > 0 else 0
    
        
solution = Solution()
answer = solution.orangesRotting(
    [[2,1,1],
     [1,1,0],
     [0,1,1]
     ])
print(answer)