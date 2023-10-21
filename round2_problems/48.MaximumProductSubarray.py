from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: started 2:10
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        maximum = curr_max

        for i in range(1, len(nums)):
            prev_max = curr_max
            curr_max = max(nums[i] * curr_min, max(nums[i], nums[i] * curr_max))
            curr_min = min(nums[i] * prev_max, min(nums[i], nums[i] * curr_min))

            maximum = max(maximum, curr_max)

        return maximum
        
solution = Solution()
answer = solution.maxProduct([2,3,-2,4,-2,3])
#answer = solution.maxProduct([2,3,-2,4])
print(answer)