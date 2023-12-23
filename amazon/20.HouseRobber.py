from typing import List

# https://leetcode.com/problems/house-robber/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:07
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            rob_this = nums[i] + dfs(i + 2)
            skip_this = dfs(i + 1)

            memo[i] = max(rob_this, skip_this)

            return memo[i]

        return dfs(0)

        
solution = Solution()
answer = solution.rob([1,2,3,1])
print(answer)