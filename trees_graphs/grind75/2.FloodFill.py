from typing import List

# https://leetcode.com/problems/flood-fill/
# Tags: graph, matrix, flood fill
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        return self.rec(image, sr, sc, color, startingColor)

    def rec(self, image: List[List[int]], sr: int, sc: int, color: int, startingColor: int) -> List[List[int]]:
        # base case
        if (image[sr][sc] != startingColor or color == startingColor):
            return image
        
        # paint the target cell the specified color
        image[sr][sc] = color

        # recursive case. Expands in 4 directions
        if (sr > 0):
            self.rec(image, sr - 1, sc, color, startingColor)
        if (sr < len(image) - 1):
            self.rec(image, sr + 1, sc, color, startingColor)
        if (sc > 0):
            self.rec(image, sr, sc - 1, color, startingColor)
        if (sc < len(image[0]) - 1):
            self.rec(image, sr, sc + 1, color, startingColor)

        return image


        
solution = Solution()
answer = solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0)
print(answer)
answer = solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(answer)

# Example: color = 2, sr = 1, sc = 1
# [1, 1, 1]
# [1, 1, 0]
# [1, 0, 1]
#
# [1, 1, 1]
# [1, 2, 0]
# [1, 0, 1]
#
# [1, 2, 1]
# [1, 2, 0]
# [1, 0, 1]
#
# [2, 2, 1]
# [1, 2, 0]
# [1, 0, 1]
#
# [2, 2, 1]
# [2, 2, 0]
# [1, 0, 1]
#
# [2, 2, 1]
# [2, 2, 0]
# [2, 0, 1]
#
# [2, 2, 2]
# [2, 2, 0]
# [2, 0, 1]