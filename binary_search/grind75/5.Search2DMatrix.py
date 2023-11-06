from typing import List
import bisect

# https://leetcode.com/problems/search-a-2d-matrix/
# Tags: binary search, matrix
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(m) where m is the max height of the grid
    # Time: 10:00
    #
    # Perform binary search on matrix by searching on a vertical slice of the first column first. Then
    # searching within that specific row
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        vertical_slice = [0] * height
        for i in range(height):
            vertical_slice[i] = matrix[i][0]

        row = bisect.bisect_right(vertical_slice, target) - 1
        index = bisect.bisect_right(matrix[row], target) - 1

        return matrix[row][index] == target

        
solution = Solution()
answer = solution.searchMatrix(
    [[1,3,5,7],
     [10,11,16,20],
     [23,30,34,60]]
, 31)
print(answer)