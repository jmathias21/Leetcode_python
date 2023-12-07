from typing import List
from collections import defaultdict

# https://leetcode.com/problems/subarray-sum-equals-k/
# Tags: Prefix Sum
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 30:00
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        s = 0
        for num in nums:
            s += num

            if s - k in prefix_sum:
                total += prefix_sum[s - k]

            prefix_sum[s] += 1

        return total
        
solution = Solution()
answer = solution.subarraySum([1,2,1,2,1], 3)
answer = solution.subarraySum([1,1,2,3,4], 6)
answer = solution.subarraySum([1,2,3], 3)
print(answer)