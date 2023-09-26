from typing import List

# https://leetcode.com/problems/number-of-islands/
# Tags: DFS, matrix, graph
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 33:00
    #
    # This solution loops through the grid until it finds an island element that
    # haven't visited yet, and then performs a DFS recursive search for connected island
    # elements until we find the entire island and add it to our visited elements. Then
    # continue our primary loop until we find another unvisited island element, until we
    # find all of the islands
    def numIslandsUsingDFS(self, grid: List[List[str]]) -> int:
        # keep track of island count
        island_count = 0
        visited = [[False for _ in row] for row in grid]

        # for each node that hasn't been visited...
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '0':
                    continue

                if not visited[row][col]:
                    self.search(grid, row, col, visited)
                    island_count += 1

        return island_count


    def search(self, grid, row, col, visited):        
        # check if in-bounds
        if row < 0 or col <  0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
            return
        
        # verify this element is part of an island and we haven't visited it yet
        if visited[row][col] or grid[row][col] != '1':
            return
        
        visited[row][col] = True

        self.search(grid, row - 1, col, visited)
        self.search(grid, row + 1, col, visited)
        self.search(grid, row, col - 1, visited)
        self.search(grid, row, col + 1, visited)


        
solution = Solution()

grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
answer = solution.numIslands(grid1)
print(answer)