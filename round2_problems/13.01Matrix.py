from collections import deque
from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 29:00
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # find all 1's
        # initiate bfs to find distance

        queue = deque()
        visited = set()
        matrix = [[-1 for _ in mat[0]] for _ in mat]
        height = len(mat)
        width = len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    matrix[i][j] = 0
                    queue.append((0, i, j))

        while queue:
            (n, i, j) = queue.popleft()

            if (i, j) in visited:
                continue
             
            matrix[i][j] = n
            visited.add((i, j))

            if i + 1 < height and mat[i + 1][j] != 0:
                queue.append((n + 1, i + 1, j))
            if i - 1 >= 0 and mat[i - 1][j] != 0:
                queue.append((n + 1, i - 1, j))
            if j + 1 < width and mat[i][j + 1] != 0:
                queue.append((n + 1, i, j + 1))
            if j - 1 >= 0 and mat[i][j - 1] != 0: 
                queue.append((n + 1, i, j - 1))

        return matrix



        
solution = Solution()
answer = solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
print(answer)