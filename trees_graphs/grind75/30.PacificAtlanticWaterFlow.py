from typing import List
from collections import deque

# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Tags: Intersection of two sets, DFS, 
class Solution:

    # Runtime Complexity: O(M * N)
    # Space Complexity: O(M * N)
    # Time: Not timed
    #
    # Use two sets that represent x, y coordinates that can reach the pacific or atlantic. For each
    # coordinate that's touching an ocean, perform a DFS that recursively traverses the island while
    # skipping coordinates that are heigher than the current coordinate. For each node traversed, we add
    # it to our specific ocean set (atlantic or pacific). When we're done we have two sets of coordinates
    # that represent all coordinates that can reach the pacific or the atlantic. Return the intersection of
    # both to get our answer
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width = len(heights[0])
        height = len(heights)
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, reachable):
            reachable.add((row, col))
            for r_mod, c_mod in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rx, cx = row + r_mod, col + c_mod
                if rx < 0 or cx < 0 or rx >= height or cx >= width:
                    continue
                if (rx, cx) in reachable:
                    continue
                if heights[row][col] > heights[rx][cx]:
                    continue
                
                dfs(rx, cx, reachable)

        for i in range(height):
            dfs(i, 0, pacific_reachable)
            dfs(i, width - 1, atlantic_reachable)
        for i in range(width):
            dfs(0, i, pacific_reachable)
            dfs(height - 1, i, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))

        
solution = Solution()
answer = solution.pacificAtlantic(
    [[3,4,5],
     [3,7,3],
     [1,1,2]]
)
answer = solution.pacificAtlantic(
    [[1,2,2,3,5],
     [3,2,3,4,4],
     [2,4,5,3,1],
     [6,7,1,4,5],
     [5,1,1,2,4]]
)
print(answer)