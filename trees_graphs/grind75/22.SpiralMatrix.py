from typing import List

# https://leetcode.com/problems/spiral-matrix/
# Tags: Matrix, Matrices, Boundary Conditions
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 50:00
    #
    # starts at the top left of the matrix and we move the [x,y] pointer to the right. When we
    # hit a boundary or a visited element, we move the direction clockwise and continue until
    # all elements have been visited and added to the output
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        total_elements = m * n
        dir = 1

        output = []

        x, y = 0, 0
        dir_mod = {
            0: (0, -1),
            1: (1, 0),
            2: (0, 1),
            3: (-1, 0),
        }

        while len(output) < total_elements:
            if x >= 0 and y >= 0 and x < m and y < n and matrix[y][x] != -999:
                output.append(matrix[y][x])
                matrix[y][x] = -999
            else:
                x -= x_mod
                y -= y_mod
                dir += 1

            x_mod, y_mod = dir_mod[dir % 4]
            x += x_mod
            y += y_mod

        return output
            

        
solution = Solution()
answer = solution.spiralOrder([[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]])
answer = solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
answer = solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
answer = solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(answer)