from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 7:34
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            
        
solution = Solution()
answer = solution.lengthOfLIS()
print(answer)