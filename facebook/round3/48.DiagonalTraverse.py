from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 5:14
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        width = len(mat[0])
        height = len(mat)

        dir = 1
        r = c = 0
        result = []

        while r != height - 1 or c != width - 1:
            result.append(mat[r][c])

            if dir == 1:
                if c + 1 >= width:
                    r += 1
                    dir = -1
                elif r - 1 < 0:
                    c += 1
                    dir = -1
                else:
                    r -= 1
                    c += 1
                continue

            if dir == -1:
                if r + 1 >= height:
                    c += 1
                    dir = 1
                elif c - 1 < 0:
                    r += 1
                    dir = 1
                else:
                    r += 1
                    c -= 1
                continue

        return result + [mat[height - 1][width - 1]]
        
solution = Solution()
answer = solution.findDiagonalOrder(
    [[1,2,3],
     [4,5,6],
     [7,8,9]])
print(answer)