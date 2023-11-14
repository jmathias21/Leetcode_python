from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:21
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        queue = deque([(0, 0, 0)])
        seen = [[False for _ in range(604)] for _ in range(604)]

        while queue:
            row, col, depth = queue.popleft()

            if row == x and col == y:
                return depth
            
            if seen[row][col]:
                continue
            seen[row][col] = True

            for row_mod, col_mod in [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]:
                new_row = row + row_mod
                new_col = col + col_mod

                if seen[new_row][new_col]:
                    continue

                queue.append((new_row, new_col, depth + 1))

        # should never happen
        return -1

        
solution = Solution()
answer = solution.minKnightMoves(270, -21)
answer = solution.minKnightMoves(5, 5)
print(answer)