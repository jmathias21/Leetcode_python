# https://leetcode.com/problems/climbing-stairs/
# Tags: Dynamic Programming, Fibonacci
class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Climbing stairs represents a fibonacci problem because the 
    # sum of n = 1 and n = 2 can be used to calculate n = 3. Fibonacci's sequence
    # falls under the category of Dynamic Programming, because we can break
    # the solution down into smaller problems
    def climbStairsFibonacciSequence(self, n: int) -> int:
        if (n == 1):
            return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n - 1]
        
        
solution = Solution()
answer = solution.climbStairs(5)
print(answer)