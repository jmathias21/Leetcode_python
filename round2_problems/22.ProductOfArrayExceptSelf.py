from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 25:00
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_nums = [1] * len(nums)
        prefix_nums[0] = nums[0]
        postfix_nums = [1] * (len(nums) + 1)
        postfix_nums[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            prefix_nums[i] = nums[i] * prefix_nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            postfix_nums[i] = nums[i] * postfix_nums[i + 1]

        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                nums[0] = postfix_nums[i + 1]
            else:
                nums[i] = prefix_nums[i - 1] * postfix_nums[i + 1]

        return nums

        
solution = Solution()
answer = solution.productExceptSelf([1,2,3,4])
print(answer)