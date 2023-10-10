from typing import List

# https://leetcode.com/problems/unique-paths/
# Tags: Dynamic programming, n choose k
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(n * m)
    # Time: Not timed
    #
    # Given our destination square (bottom-right), we know that if our robot started one square to the left
    # or one square above it, that there would only be one possible path from each of those squares to the
    # destination. Given this, we know that if we started to the upper left of the destination square, there
    # are two possible paths to the destination. This is the sub-problem in our DP solution.
    #
    # For this solution, we pre-populate a DP matrix with 1's, and then loop through squares not by the edges,
    # while using the edges as our solved sub-problems to calculate our current square, and saving it back to
    # our DP matrix. In essence, we're solving this problems backwards by treating the robot as the destination
    # and the destination as our robot, but it doesn't matter because it results in the same answer
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]
        

solution = Solution()
answer = solution.uniquePaths(3, 2)
answer = solution.uniquePaths2(3, 7)
print(answer)