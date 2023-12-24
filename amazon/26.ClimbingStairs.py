from typing import List

# 
# Tags: 
class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i > n:
                return 0 
            if i == n:
                return 1
            
            total = 0
            total += dfs(i + 1)
            total += dfs(i + 2)

            memo[i] = total

            return total
        
        result = dfs(0)
        return result


    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 3:52
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]



        
solution = Solution()
answer = solution.climbStairs(3)
print(answer)