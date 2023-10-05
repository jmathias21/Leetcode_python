# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 23:00
    def climbStairs(self, n: int) -> int:
        # 1, 1, 2, 3, 5, 8, 13, etc.
        total_ways = 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n]

        
solution = Solution()
answer = solution.climbStairs(2)
#answer = solution.climbStairs(10)
print(answer)