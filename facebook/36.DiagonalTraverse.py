from typing import List

# https://leetcode.com/problems/diagonal-traverse/
# Tags: 
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(1)
    # Time: 22:00
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        w = len(mat[0])
        h = len(mat)
        output = []
        r = c = 0

        go_up = True
        while r != h - 1 or c != w - 1:
            output.append(mat[r][c])

            if go_up:
                if c + 1 >= w:
                    r += 1
                    go_up = False
                elif r - 1 < 0:
                    c += 1
                    go_up = False
                else:
                    r -= 1
                    c += 1
                continue
            else:
                if r + 1 >= h:
                    c += 1
                    go_up = True
                elif c - 1 < 0:
                    r += 1
                    go_up = True
                else:
                    r += 1
                    c -= 1
                continue

        return output + [mat[h - 1][w - 1]]

        
solution = Solution()
answer = solution.findDiagonalOrder(
    [[1,2],
     [3,4]]
)
answer = solution.findDiagonalOrder(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)
print(answer)