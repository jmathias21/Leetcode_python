from typing import List

# https://leetcode.com/problems/house-robber/
# Tags: Bottom-up dynamic programming
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 22:00
    #
    # Uses bottom-up DP. At each step, the robber has two options: Pick the current house and skip
    # the next house, or pick the next house and skip the current house. This looks like the formula:
    # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]). If we skip the current house, that's dp[i - 1]
    # because we're taking our current total and waiting. If we take the current house, then that's
    # dp[i - 2] + nums[i], because we're taking our previous total and adding the new house to our
    # total
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]

        # use this in place of a DP array because we only need the last two totals
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, length):
            new_max = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = new_max

        return prev1

        
solution = Solution()
answer = solution.rob([1,2,3,1])
answer = solution.rob([3,2,5,10,1,3,6,4,8,5])
print(answer)