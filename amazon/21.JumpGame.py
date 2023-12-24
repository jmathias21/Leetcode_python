from typing import List

# https://leetcode.com/problems/jump-game/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:31
    def canJump(self, nums: List[int]) -> bool:
        furthest_jump = 0

        i = 0
        while i <= furthest_jump:
            furthest_jump = max(furthest_jump, i + nums[i])
            if furthest_jump >= len(nums) - 1:
                return True
            i += 1

        return False

        
solution = Solution()
answer = solution.canJump([2,3,1,1,4])
print(answer)