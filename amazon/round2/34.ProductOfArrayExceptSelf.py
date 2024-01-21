from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_sum = [0] * len(nums)
        product_sum[0] = nums[0]

        for i in range(1, len(nums)):
            product_sum[i] = product_sum[i - 1] * nums[i]

        result = [0] * len(nums)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix = product_sum[i - 1] if i > 0 else 1
            result[i] = prefix * postfix
            postfix *= nums[i]

        return result

        
solution = Solution()
answer = solution.productExceptSelf([1,2,3,4]) # [24,12,8,6]
answer = solution.productExceptSelf([1,1,2,1]) # [2,2,1,2]
print(answer)