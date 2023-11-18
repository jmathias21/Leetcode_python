from typing import List

# https://leetcode.com/problems/jump-game/
# Tags: Greedy
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(1)
    # Time: 53:00
    #
    # For each number, calculate how far we can jump. If any of the numbers can jump to or past
    # the last index, then we return true. However, we only check numbers with an index less
    # than or equal to the furthest index we've jumped to. This prevents us from checking numbers
    # that are impossible to jump to
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        furthest_jump = 0

        i = 0
        while i <= furthest_jump:
            furthest_jump = max(furthest_jump, i + nums[i])
            if furthest_jump >= length - 1:
                return True
            i += 1
            
        return False

        
solution = Solution()
answer = solution.canJump([3,2,1,0,4])
answer = solution.canJump([2,3,1,1,4])
answer = solution.canJump([3,5,7,1,1,0,0,0,0,1])
print(answer)