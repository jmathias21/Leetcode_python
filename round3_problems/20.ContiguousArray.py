from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:38
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        max_length = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in d:
                max_length = max(max_length, i - d[count])
            else:
                d[count] = i

        return max_length
        
solution = Solution()
#answer = solution.findMaxLength([0,1])
answer = solution.findMaxLength([0,0,1,0,0,0,1,1])
answer = solution.findMaxLength([0,1,1,0,0,1,0,0,1,1])
print(answer)