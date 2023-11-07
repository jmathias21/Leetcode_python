from typing import List

# https://leetcode.com/problems/combination-sum-iv/
# Tags: DFS, top-down dynamic programming
class Solution:

    # Runtime Complexity: O(T * n) where T is the target
    # Space Complexity: O(T)
    # Time: Not timed
    #
    # Perform DFS to build up combinations of sums. Use memoization to track the number of results
    # for the given sum so that if we see that sum again we immediately know how many results there are
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def dfs(sum):
            if sum in memo:
                return memo[sum]

            if sum == target:
                return 1
            
            result = 0
            for num in nums:
                if sum + num <= target:
                    result += dfs(sum + num)
                else:
                    break

            memo[sum] = result
            return result

        return dfs(0)

        
solution = Solution()
answer = solution.combinationSum4([1,2], 3)
print(answer)