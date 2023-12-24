from typing import List

# https://leetcode.com/problems/unique-paths/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 20:00
    def uniquePathsUsingTopDownDP(self, m: int, n: int) -> int:
        memo = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            if row >= m or col >= n:
                return 0
            
            if row == m - 1 and col == n - 1:
                return 1
            
            total = 0
            total += dfs(row + 1, col)
            total += dfs(row, col + 1)

            memo[(row, col)] = total

            return total
        
        result = dfs(0, 0)
        return result
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]



        
solution = Solution()
answer = solution.uniquePaths(3, 7)
print(answer)