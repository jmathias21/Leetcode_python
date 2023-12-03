from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        s = 0
        answer = 0

        for i, num in enumerate(nums):
            s += num

            if s - k in prefix:
                answer += prefix[s - k]

            prefix[s] += 1

        return answer


        
solution = Solution()
answer = solution.subarraySum([1,-1,0], 0)
answer = solution.subarraySum([1,2,3], 3)
print(answer)