from typing import List

# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Tags: 
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Time: started 6:07
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width = len(heights[0])
        height = len(heights)
        atlantic_seen = set()
        pacific_seen = set()

        def dfs(row, col, seen):
            if (row, col) in seen:
                return
            
            seen.add((row, col))
            for r_mod, c_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_r, new_c = row + r_mod, col + c_mod

                if new_r < 0 or new_c < 0 or new_r >= height or new_c >= width:
                    continue

                if heights[new_r][new_c] < heights[row][col]:
                    continue

                dfs(new_r, new_c, seen)

        for row in range(height):
            dfs(row, 0, pacific_seen)
            dfs(row, width - 1, atlantic_seen)

        for col in range(width):
            dfs(0, col, pacific_seen)
            dfs(height - 1, col, atlantic_seen)

        return atlantic_seen.intersection(pacific_seen)

        
solution = Solution()
answer = solution.pacificAtlantic(
    [[1,2,2,3,5],
     [3,2,3,4,4],
     [2,4,5,3,1],
     [6,7,1,4,5],
     [5,1,1,2,4]]
)
print(answer)

# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]