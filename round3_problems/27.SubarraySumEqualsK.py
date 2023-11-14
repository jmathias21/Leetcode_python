from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 12:05
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        answer = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for i in range(len(nums)):
            s += nums[i]

            if s - k in prefix_sum:
                answer += prefix_sum[s - k]

            prefix_sum[s] += 1

        return answer

        
solution = Solution()
answer = solution.subarraySum([1,-1,0], 0)
answer = solution.subarraySum([1], 0)
answer = solution.subarraySum([1,4,2,3,2,5], 5)
print(answer)