from typing import List

# https://leetcode.com/problems/coin-change/
# Tags: 
class Solution:

    # Runtime Complexity: O(amount * n)
    # Space Complexity: O(amount)
    # Time: 28:00
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining < 0:
                return None
            
            if remaining in memo:
                return memo[remaining]
            
            if remaining == 0:
                return 1

            total = float('inf')
            for coin in coins:
                used = dfs(remaining - coin)
                if used:
                    total = min(total, used)

            memo[remaining] = total + 1

            return memo[remaining]
        
        test = dfs(amount)
        return test - 1 if test != float('inf') else -1

        
solution = Solution()
answer = solution.coinChange([1,2,5], 11)
print(answer)