from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Tags: Dynamic Programming
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    #
    # When the price in stock goes down, start keeping track
    # of the running spread each day, and store the highest spread we've seen
    def maxProfit(self, prices: List[int]) -> int:
        highestSell = 0
        lowPrice = None

        for price in prices:
            if lowPrice == None or price < lowPrice:
                lowPrice = price
            elif price > lowPrice:
                highestSell = max(highestSell, price - lowPrice)

        return highestSell

        
solution = Solution()
answer = solution.maxProfit([7,1,5,3,6,4])
print(answer)