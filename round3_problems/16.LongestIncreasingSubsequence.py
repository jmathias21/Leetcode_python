from bisect import bisect_left
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:30
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                sub[bisect_left(sub, nums[i])] = nums[i]

        return len(sub)
        

        
solution = Solution()
answer = solution.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
answer = solution.lengthOfLIS([4,10,4,3,8,9])
# answer = solution.lengthOfLIS([2,6,7,8,2,3])
answer = solution.lengthOfLIS([10,9,2,5,3,7,101,18])
print(answer)