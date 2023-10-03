from typing import List

# https://leetcode.com/problems/product-of-array-except-self/
# Resources: https://leetcode.com/problems/product-of-array-except-self/solutions/2996710/o-n-single-pass-solution-in-python-easy-to-understand/
# Tags: Prefix products, Postfix products
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        for i in range(1, length):
            # calculate the total product from left to right and store
            # it at i + 1. For example, if we have nums [1, 2, 3, 4] and
            # i = 2, then the current product is 1 * 2. This represents
            # the current prefix value
            output[i] = nums[i - 1] * output[i - 1]

        # for each prefix value now stored in the output, we can multiply it
        # by its postfix to get the total product, excluding the current
        # number i
        postfix = 1
        for i in range(length - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output

        
solution = Solution()
answer = solution.productExceptSelf([1,2,3,4]) # [24,12,8,6]
answer = solution.productExceptSelf([4,3,2,1,2]) # [12,16,24,48,24]
print(answer)

# Example: [1,2,3,4]

# Calculate the prefixes for each number and store it in output. e.g. output[3] = 1 * 2 * 3
# output = [1, 1, 2, 6]

# loop through numbers from right to left and calculate the final product by multiplying the
# postfix by the prefix
# output = [1, 1, 2, 6 * postfix] = [1, 1, 2, 6 * 1] = [1, 1, 2, 6]
# output = [1, 1, 2 * postfix, 6] = [1, 1, 2 * 4, 6] = [1, 1, 8, 6]
# output = [1, 1 * postfix, 2, 6] = [1, 1 * 12, 2, 6] = [1, 12, 8, 6]
# output = [1 * postfix, 1, 2, 6] = [1 * 24, 1, 2, 6] = [24, 12, 8, 6]