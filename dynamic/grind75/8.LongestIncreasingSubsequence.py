from typing import List

# https://leetcode.com/problems/longest-increasing-subsequence/
# Tags: Dynamic Programming
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Uses bottom-up dynamic programming. At the first element we know the LIS is 1. At the second element,
    # we know the LIS is LIS(0) + 1 if num is greater than the first element, or 1 if not. At the third element, the LIS is
    # max(LIS(2), LIS(0) + 1, LIS(1) + 1), and so on. This means that at every iteration, we must look at all previous LIS's
    # where the number is smaller than the current number and get the max off all of them.
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


solution = Solution()
answer = solution.lengthOfLIS([4,10,4,3,8,9]) # 3
answer = solution.lengthOfLIS([0,1,0,3,2,3]) # 2
answer = solution.lengthOfLIS([10,9,2,5,3,7,101,18]) # 4
print(answer)

# Example: [1,2,4,3]
#
#  1, 2, 4, 3
# [1, 1, 1, 1]

# 2 > 1, nums[1] = nums[0] + 1
#  1, 2, 4, 3
# [1, 2, 1, 1]

# 4 > 1, nums[2] = nums[0] + 1
#  1, 2, 4, 3
# [1, 2, 2, 1]

# 4 > 2, nums[2] = nums[1] + 1
#  1, 2, 4, 3
# [1, 2, 3, 1]

# 3 > 1, nums[3] = nums[0] + 1
#  1, 2, 4, 3
# [1, 2, 3, 2]

# 3 > 2, nums[3] = nums[1] + 1
#  1, 2, 4, 3
# [1, 2, 3, 2]

# max(dp) = 3