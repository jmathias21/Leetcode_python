from typing import List

# https://leetcode.com/problems/combination-sum/
# Tags: dynamic programming
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    #
    # Uses dynamic programming. With each candidate, start with a target of 0, then 1, etc..
    # and determine all combinations of that candidate up to the target amount. Then
    # move on to the next candidate and repeat. Each candidate can subtract the current target by
    # the candidate amount and use the array at that index to add to its answer. e.g. if we
    # know that dp[4] = [2,2] because we've precomputed candidate = 2, then when we're computing
    # dp[7] for candidate 3, if we take 7 - 3, we get 4, so we can append 3 to [2,2] which gives
    # us [2,2,3]
    def combinationSumUsingDP(self, candidates, target):
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        
        for candidate in candidates:
            for i in range(candidate, target + 1):
                for combination in dp[i - candidate]:
                    dp[i].append(combination + [candidate])
                
        return dp[target]

        
solution = Solution()
answer = solution.combinationSum([2,3,6,7], 7)
print(answer)

# Example: combinationSumUsingDP
# [2,3,6,7] target = 7

# [2,3,6,7] number = 2
# target = 1, []
# target = 2, [2]
# target = 3, []
# target = 4, [2,2]
# target = 5, []
# target = 6, [2,2,2]
# target = 7, []]

# [2,3,6,7] number = 3
# target = 1, []
# target = 2, [2]
# target = 3, [3]
# target = 4, [2,2]
# target = 5, [2,3]
# target = 6, [2,2,2], [3,3]
# target = 7, [2,2,3]

# [2,3,6,7] number = 6
# target = 1, []
# target = 2, [2]
# target = 3, [3]
# target = 4, [2,2]
# target = 5, [2,3]
# target = 6, [2,2,2], [3,3], [6]
# target = 7, [2,2,3]

# [2,3,6,7] number = 7
# target = 1, []
# target = 2, [2]
# target = 3, [3]
# target = 4, [2,2]
# target = 5, [2,3]
# target = 6, [2,2,2], [3,3], [6]
# target = 7, [2,2,3], [7]