from typing import List

# https://leetcode.com/problems/maximal-square/
# Tags: Dynamic programming, bottom up
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Time: Not timed
    #
    # Create a 2d DP array that mimics the size of the matrix. Iterate through the matrix from top-left to bottom -left.
    # If all elements to the left, upper left, and above the current cell are 1's, then we know its a square. The size
    # of the square though is dependent on what we have stored in our DP matrix. If, for example, the min size is 2 in adjacent
    # cells, we increase it by 1. At the end, we square the size to get the maximum square size
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        width, height = len(matrix[0]), len(matrix)
        dp = [[0] * width for _ in range(height)]
        maximum = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    dp[row][col] = 1
                    if row > 0 and col > 0:
                        # check left, upper left, and top cell for the min size. Increase by 1 in the current cell
                        dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
                    maximum = max(maximum, dp[row][col])
                    
        return maximum ** 2



solution = Solution()
answer = solution.maximalSquare(
    [["0","1"],
     ["1","0"]])
print(answer)

answer = solution.maximalSquare(
    [["1","0","1","0","0"]
     ,["1","0","1","1","1"]
     ,["1","1","1","1","1"]
     ,["1","0","1","1","1"]])
print(answer)