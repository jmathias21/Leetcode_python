from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 6:00
    def maxProfit(self, prices: List[int]) -> int:
        smallest = 0
        max_profit = 0

        for i, price in enumerate(prices):
            if price > prices[smallest]:
                max_profit = max(max_profit, price - prices[smallest])
            else:
                smallest = i

        return max_profit

        
solution = Solution()
answer = solution.maxProfit([7,1,5,3,6,4])
print(answer)