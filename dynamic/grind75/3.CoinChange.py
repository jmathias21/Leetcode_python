from typing import List

# https://leetcode.com/problems/coin-change/description/
# Resources: https://www.youtube.com/watch?v=jgiZlGzXMBw
# Tags: Dynamic programming, unbounded knapsack, bottom up
class Solution:

    # Runtime Complexity: O(n * m) where n = amount and m = coins
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Uses a bottom up dynamic programming (knapsack unbounded) approach
    # to calculate the minimum coins needed for each amount, 0, 1, 2...
    # all the way up to amount. Doing this for each amount, for each coin,
    # allows us to eventually find the minimum for our target amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize an array that will keep track of the minimum coins
        # needed for each amount, where the amount needed for a specific
        # element is equal to its index. e.g. dp[3] will require the
        # minimum amount of coins that add to 3. We set each index value
        # to amount + 1, which is just an arbitrarily high value to indicate
        # it hasn't been set yet.
        dp, dp[0] = [amount + 1] * (amount + 1), 0

        # for each amount, we calculate the minimum coins needed by subtracting
        # the coin value from the current amount and adding 1. For example, if
        # we are calculating minimum values for coin 1, and we know that dp[6]
        # requires a minimum of 2 coins (e.g. coins 5 and 1), then we know that
        # dp[7] = dp[current_amount - current_coin_value] + 1 = dp[7 - 1] + 1 = 3.
        # Then we take the minimum value after analyzing all potential coins, and
        # keep doing this all the way up to the amount we're trying to solve for
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])

        # if the last amount in dp was never set, it means that there are no coins
        # that add up to that amount, so we return -1, otherwise we return the minimum
        # coins needed for that amount
        return dp[amount] if dp[amount] < amount + 1 else -1
        
        
solution = Solution()
answer = solution.coinChange([1,2,5], 11)
answer = solution.coinChange([186,419,83,408], 6249)
answer = solution.coinChange([2], 3)
print(answer)

# Example: coins = [1,2,5], amount = 11
# dp = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

# For coin 1
#   dp[1] = min(dp[1 - 1] + 1, 12) = 1
#   dp[2] = min(dp[2 - 1] + 1, 12) = 2
#   dp[3] = min(dp[2 - 1] + 1, 12) = 3
#   dp[4] = min(dp[2 - 1] + 1, 12) = 4
#   dp[5] = min(dp[2 - 1] + 1, 12) = 5
#   dp[6] = min(dp[2 - 1] + 1, 12) = 6
#   dp[7] = min(dp[2 - 1] + 1, 12) = 7
#   dp[8] = min(dp[2 - 1] + 1, 12) = 8
#   dp[9] = min(dp[2 - 1] + 1, 12) = 9
#   dp[10] = min(dp[2 - 1] + 1, 12) = 10
#   dp[11] = min(dp[2 - 1] + 1, 12) = 11
#   dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# For coin 2
#   dp[2] = min(dp[2 - 2] + 1, 2) = 1
#   dp[3] = min(dp[3 - 2] + 1, 3) = 2
#   dp[4] = min(dp[4 - 2] + 1, 4) = 2
#   dp[5] = min(dp[5 - 2] + 1, 4) = 3
#   dp[6] = min(dp[6 - 2] + 1, 4) = 3
#   dp[7] = min(dp[7 - 2] + 1, 4) = 4
#   dp[8] = min(dp[8 - 2] + 1, 4) = 4
#   dp[9] = min(dp[9 - 2] + 1, 4) = 5
#   dp[10] = min(dp[10 - 2] + 1, 4) = 5
#   dp[11] = min(dp[11 - 2] + 1, 4) = 6
#   dp = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

# For coin 5
#   dp[5] = min(dp[5 - 5] + 1, 2) = 1
#   dp[6] = min(dp[6 - 5] + 1, 2) = 2
#   dp[7] = min(dp[7 - 5] + 1, 2) = 2
#   dp[8] = min(dp[8 - 5] + 1, 2) = 3
#   dp[9] = min(dp[9 - 5] + 1, 2) = 3
#   dp[10] = min(dp[10 - 5] + 1, 2) = 2
#   dp[11] = min(dp[11 - 5] + 1, 2) = 3
#   dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]

# answer = dp[11] = 3