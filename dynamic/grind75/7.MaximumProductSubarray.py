from typing import List

# https://leetcode.com/problems/maximum-product-subarray/
# Tags: Bottom-up Dynamic Programming, Kadane's Algorithm
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Track the current maximum and the current minimum every step, where the max is the larger value between
    # the current number and the previous maximum multiplied by the current number. For the min we take the
    # smaller number. In cases where a negative number will make the min larger than the max, we flip them so
    # that the max is always larger than the min. At the end, we return the largest maximum that we saw
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        curr_max = nums[0]
        curr_min = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            prev_max = curr_max

            # If the current max = -2 and num = 4, the new max becomes 4 because its higher than -8.
            # If the current max is 2, current min = -6, and num = -4, the new max becomes 24 because
            # -6 * -4 is higher than -4 and higher than 2 * -4
            curr_max = max(curr_min * nums[i], nums[i], curr_max * nums[i])

            curr_min = min(prev_max * nums[i], min(nums[i], curr_min * nums[i]))

            max_product = max(max_product, curr_max)

        return max_product


        
solution = Solution()
answer = solution.maxProduct([-2])
answer = solution.maxProduct([2,3,-2,0,-2,4,-5])
answer = solution.maxProduct([3,-1,4])
answer = solution.maxProduct([2,3,-2,4])
print(answer)