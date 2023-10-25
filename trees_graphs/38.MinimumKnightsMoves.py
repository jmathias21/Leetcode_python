from collections import deque
from functools import lru_cache

# https://leetcode.com/problems/minimum-knight-moves/
# Tags: 
class Solution:

    # Runtime Complexity: O(max(|x|,|y|) ^ 2)
    # Space Complexity: O(max(|x|,|y|) ^ 2)
    # Time: Not timed
    #
    # Uses BFS to recursively check every possible position. We use a grid to track 
    # seen nodes instead of a set because it uses less memory
    def minKnightMovesUsingBFS(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        max_size = 604 # max range with some extra padding

        seen = [[False for _ in range(max_size)] for _ in range(max_size)]

        queue = deque([(0,0,0)])

        while queue:
            row, col, depth = queue.popleft()

            if row == y and col == x:
                return depth

            for row_mod, col_mod in [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                new_row = row + row_mod
                new_col = col + col_mod

                if seen[new_row][new_col]:
                    continue

                seen[new_row][new_col] = True
                queue.append((new_row, new_col, depth + 1))

        return -1

    # Runtime Complexity: O(max(|x|,|y|) ^ 2)
    # Space Complexity: O(max(|x|,|y|) ^ 2)
    # Time: Not timed
    def minKnightMovesUsingDFS(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(abs(x), abs(y))

        
solution = Solution()
#answer = solution.minKnightMovesUsingDFS(1, 1)
answer = solution.minKnightMovesUsingDFS(2, 112)
answer = solution.minKnightMovesUsingDFS(2, 1)
print(answer)