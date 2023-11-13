from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def fibUsingTopDown(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        def dfs(n):
            if n in memo:
                return memo[n]
            
            memo[n] = dfs(n - 1) + dfs(n - 2)

            return memo[n]

        dfs(n)
        return memo[n]


    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def fibUsingBottomUp(self, n: int) -> int:
        if n <= 1:
            return n

        memo = [0] * (n + 1)
        memo[1] = 1

        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]
        
solution = Solution()
answer = solution.fibUsingBottomUp(2)
answer = solution.fibUsingBottomUp(8)
print(answer)