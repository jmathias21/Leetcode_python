from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: not timed
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        s = 0

        for i in range(len(nums)):
            s += nums[i]

            diff = s - k

            if diff in prefix:
                answer += prefix[diff]

            prefix[s] += 1

        return answer

        
solution = Solution()
#answer = solution.subarraySum([-1,-1,1], 0)
answer = solution.subarraySum([5,3,1,8,2,4,4], 8)
print(answer)

# 5, 3, 1, 8, 2, 4, 4
# 5, 8, 9, 17,19,23,27