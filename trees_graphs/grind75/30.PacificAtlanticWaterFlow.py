from typing import List

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
        width, height = len(heights[0]), len(heights)
        pacific_reached = set()
        atlantic_reached = set()

        def dfs(row, col, reached):
            reached.add((row, col))
            for row_mod, col_mod in ([-1, 0], [1, 0], [0, -1], [0, 1]):
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if (new_row, new_col) in reached:
                    continue

                if heights[row][col] > heights[new_row][new_col]:
                    continue

                dfs(new_row, new_col, reached)

        # start DFS search from coordinates that are touching one of the oceans
        for y in range(height):
            dfs(y, 0, pacific_reached)
            dfs(y, width - 1, atlantic_reached)
        for x in range(width):
            dfs(0, x, pacific_reached)
            dfs(height - 1, x, atlantic_reached)

        return list(pacific_reached.intersection(atlantic_reached))

        
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