from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:53
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1 
        
solution = Solution()
#answer = solution.coinChange([2,5,10,1], 27)
#answer = solution.coinChange([2,5], 11)
answer = solution.coinChange([1,2,5], 11)
print(answer)