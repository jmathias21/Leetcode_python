from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 4:10
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0,0,0)])
        x = abs(x)
        y = abs(y)

        size = 604
        seen = [[False for _ in range(size)] for _ in range(size)]

        while queue:
            row, col, depth = queue.popleft()

            if seen[row][col]:
                continue

            dist = (x - col) + (y - row)
            if dist == 2:
                return depth + 2
            if row == y and col == x:
                return depth
            
            seen[row][col] = True

            for row_mod, col_mod in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]:
                new_row = row + row_mod
                new_col = col + col_mod
                queue.append((new_row, new_col, depth + 1))

        return -1


        
solution = Solution()
answer = solution.minKnightMoves(270,-21)
answer = solution.minKnightMoves(4,3)
answer = solution.minKnightMoves(1,1)
answer = solution.minKnightMoves(5,5)
print(answer)