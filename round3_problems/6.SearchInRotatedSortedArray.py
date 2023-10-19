import bisect
from typing import List

# 
# Tags: 
class Solution:
    
    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 3:12, 5:37
    def search2(self, nums: List[int], target: int) -> int:
        # binary search for the rotation point
        # binary search over fixed array
        n = len(nums)
        left, right = 0, n - 1

        left_anchor = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        rotation_index = left
        if rotation_index == 0:
            target_index = bisect.bisect_left(nums, target)
        elif target < left_anchor:
            target_index = bisect.bisect_left(nums[rotation_index:], target) + rotation_index
        else:
            target_index = bisect.bisect_left(nums[:rotation_index], target)

        return target_index if target_index < len(nums) and nums[target_index] == target else -1


        
solution = Solution()
answer = solution.search([3,5,1], 3)
answer = solution.search([3,1], 1)
answer = solution.search([4,5,6,7,0,1,2], 0)
answer = solution.search([4,5,6,7,0,1,2], 3)
answer = solution.search([4,5,6,7,0,1,2], 2)

# [4,5,6,7,8,1,2]
# [1,2,4,5,6,7,8]

print(answer)