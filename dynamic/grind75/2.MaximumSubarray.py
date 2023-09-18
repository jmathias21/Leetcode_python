from typing import List

# https://leetcode.com/problems/maximum-subarray/
# Tags: dynamic programming, kadane's algorithm
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 45:00
    #
    # Use dynamic programming to track both the current sum
    # and the max sum we've seen as we iterate through the array.
    # If at any point we see that the current sum is smaller than
    # the number at the current index, we just restart our sum at that
    # index
    def maxSubArray(self, nums: List[int]) -> int:
        curr_largest_sum = max_largest_sum = nums[0]

        for i in range(1, len(nums)):
            curr_largest_sum = max(curr_largest_sum + nums[i], nums[i])
            max_largest_sum = max(curr_largest_sum, max_largest_sum)

        return max_largest_sum

        
solution = Solution()
answer = solution.maxSubArray([1])
answer = solution.maxSubArray([-2, 1])
answer = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
answer = solution.maxSubArray([-1, 2, 3, -2, 6])
print(answer)

# [-1, 2, 3, -2, 6]
# curr_largest_sum = -1
# max_largest_sum = -1

# -1, 2
# curr_largest_sum = 2
# max_largest_sum = 2

# 2, 3
# curr_largest_sum = 5
# max_largest_sum = 5

# 5, -2
# curr_largest_sum = 3
# max_largest_sum = 5

# 3, 6
# curr_largest_sum = 9
# max_largest_sum = 9