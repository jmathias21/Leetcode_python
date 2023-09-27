from typing import List

# https://leetcode.com/problems/combination-sum/
# Resources: https://www.youtube.com/watch?v=GBKI9VSKdGg
# Tags: backtracking, dynamic programming, DFS
class Solution:

    # Runtime Complexity: O(N^(T/M + 1)) where N is the total number of candidates, M is the minimum
    # candidate value, and T is the target
    # Space Complexity: O(T/M)
    # Time: Not timed
    #
    # Uses DFS recursive backtracking to incrementally build candidates to the solution
    # while dropping candidates that we don't want to retry
    def combinationSumUsingBacktrackingRec(self, candidates, target):
        answer = []

        def dfs(i, cur, sum):
            if sum == target:
                answer.append(cur.copy())
                return
            if i >= len(candidates) or sum > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, sum + candidates[i]) # left
            cur.pop()
            dfs(i + 1, cur, sum) # right

        dfs(0, [], 0)
        return answer
        

    # Runtime Complexity: O(N * T * K) where N is the number of candidates, T is the target, and K is the maximum
    # number of occurrences of a candidate in a combination sum
    # Space Complexity: O(N * T)
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
        dp[0] = [[]]

        for candidate in candidates:
            for i in range(candidate, target + 1):
                # find previous combinations that we know are equal to i (the current target)
                # minus the candidate. This gives us a combination that, when we apply our
                # candidate, will add up exactly to the target
                for combination in dp[i - candidate]:
                    dp[i].append(combination + [candidate])

        return dp[target]

        
solution = Solution()
answer = solution.combinationSumUsingBacktrackingRec([8,7,4,3], 11)
#answer = solution.combinationSumUsingBacktrackingRec([2,3,6,7], 7)
print(answer)

#

# Example: combinationSumUsingDP
# [2,3,6,7] target = 7

# [2,3,6,7] candidate = 2
# target = 1, []
# target = 2, [2]
# target = 3, []
# target = 4, [2,2]
# target = 5, []
# target = 6, [2,2,2]
# target = 7, []]

# [2,3,6,7] candidate = 3
# target = 1, []
# target = 2, [2]
# target = 3, [3]
# target = 4, [2,2]
# target = 5, [2,3]
# target = 6, [2,2,2], [3,3]
# target = 7, [2,2,3]

# [2,3,6,7] candidate = 6
# target = 1, []
# target = 2, [2]
# target = 3, [3]
# target = 4, [2,2]
# target = 5, [2,3]
# target = 6, [2,2,2], [3,3], [6]
# target = 7, [2,2,3]

# [2,3,6,7] candidate = 7
# target = 1, []
# target = 2, [2]
# target = 3, [3]
# target = 4, [2,2]
# target = 5, [2,3]
# target = 6, [2,2,2], [3,3], [6]
# target = 7, [2,2,3], [7]