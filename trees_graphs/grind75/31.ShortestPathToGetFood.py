from collections import deque
from typing import List

# https://leetcode.com/problems/shortest-path-to-get-food/
# Tags: BFS
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 27:00
    #
    # Use BFS while skipping visited nodes, walls, and out-of-bounds positions. Track the current
    # depth and return the current depth when we find the first instance of food
    def getFood(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        seen = [[False for _ in range(width)] for _ in range(height)]
        queue = deque()

        for row in range(height):
            for col in range(width):
                if grid[row][col] == '*':
                    queue.append((row, col, 0))
                    break
            else:
                continue
            break

        while queue:
            row, col, depth = queue.popleft()

            if grid[row][col] == '#':
                return depth
            
            if seen[row][col]:
                continue

            seen[row][col] = True
            for row_mod, col_mod in ([1,0],[-1,0],[0,1],[0,-1]):
                new_row = row + row_mod
                new_col = col + col_mod
                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if grid[new_row][new_col] == 'X':
                    continue

                if seen[new_row][new_col]:
                    continue

                queue.append((new_row, new_col, depth + 1))

        return -1


        
solution = Solution()
answer = solution.getFood(
    [["X","X","X","X","X","X","X","X"],
     ["X","*","O","X","O","#","O","X"],
     ["X","O","O","X","O","O","X","X"],
     ["X","O","O","O","O","#","O","X"],
     ["X","X","X","X","X","X","X","X"]]
)
answer = solution.getFood(
    [["X","X","X","X","X","X"],
     ["X","*","O","O","O","X"],
     ["X","O","O","#","O","X"],
     ["X","X","X","X","X","X"]]
)
print(answer)