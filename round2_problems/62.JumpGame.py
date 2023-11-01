from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 10:00
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        largest = 0

        for i in range(n):
            largest -= 1
            largest = max(largest, nums[i])

            if nums[i] == 0 and largest <= 0 and i < n - 1:
                return False
            
        return True

        
solution = Solution()
answer = solution.canJump([0])
answer = solution.canJump([2,3,1,1,4])
answer = solution.canJump([3,2,1,0,4])
print(answer)