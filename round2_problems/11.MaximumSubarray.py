from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    def maxSubArray(self, nums: List[int]) -> int:
        # Move right pointer, while keeping tack of sum
        # if sum goes does, move left pointer forward

        curr_sum = nums[0]
        maximum = nums[0]
        
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            maximum = max(maximum, curr_sum)

        return maximum
                

        
solution = Solution()
answer = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(answer)