from typing import List
from collections import defaultdict

# https://leetcode.com/problems/making-a-large-island/
# Tags: DFS, Hash Map
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(n * m)
    # Time: 45:00
    def largestIsland(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        islands = {}
        sizes = defaultdict(int)

        def get_size(hash, row, col):
            if (row, col) in islands:
                return

            sizes[hash] += 1

            islands[(row, col)] = hash
            for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row, new_col = row + row_mod, col + col_mod

                if new_row < 0 or new_col < 0 or new_row >= height or new_col >= width:
                    continue

                if (new_row, new_col) in islands:
                    continue

                if grid[new_row][new_col] != 1:
                    continue

                get_size(hash, new_row, new_col)

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    get_size(len(sizes), i, j)

        largest = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    size = 1
                    sizes_added = set()
                    for row_mod, col_mod in [(1,0),(0,1),(-1,0),(0,-1)]:
                        new_row, new_col = i + row_mod, j + col_mod
                        if (new_row, new_col) in islands:
                            island_hash = islands[(new_row, new_col)]
                            if island_hash in sizes_added:
                                continue

                            size += sizes[island_hash]
                            sizes_added.add(island_hash)
                    largest = max(largest, size)

        return largest if largest > 0 else (width * height)


        
solution = Solution()
answer = solution.largestIsland(
    [[0,1,0,0],
     [0,0,1,0],
     [1,0,1,1],
     [0,0,0,0],]
)
print(answer)