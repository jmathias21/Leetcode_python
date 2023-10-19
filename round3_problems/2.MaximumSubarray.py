from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 14:00
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = 1
        curr = nums[0]
        highest = curr

        while right < len(nums):
            if curr < 0 and nums[right] > curr:
                curr = nums[right]
                left += 1
            else:
                curr += nums[right]

            right += 1
            highest = max(highest, curr)

        return highest
        
solution = Solution()
answer = solution.maxSubArray([1,2])
answer = solution.maxSubArray([-1,-2])
answer = solution.maxSubArray([-2,-1])
answer = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(answer)