from typing import List
import bisect

# https://leetcode.com/problems/longest-increasing-subsequence/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:05
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                next_highest = bisect.bisect_left(sub, nums[i])
                sub[next_highest] = nums[i]

        return len(sub)

        
solution = Solution()
answer = solution.lengthOfLIS([10,9,2,5,3,7,101,18])
print(answer)