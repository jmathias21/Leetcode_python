from typing import List
import bisect

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:22
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                i = bisect.bisect_left(stack, num)
                stack[i] = num

        return len(stack)

        
solution = Solution()
#answer = solution.lengthOfLIS([7,7,7,7,7,7,7])
answer = solution.lengthOfLIS([10,9,2,5,3,7,101,18])
print(answer)