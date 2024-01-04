from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:13
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = 0
        result = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sum:
                result += prefix_sum[curr_sum - k]

            prefix_sum[curr_sum] += 1

        return result


        
solution = Solution()
# answer = solution.subarraySum([1,1,1], 2)
answer = solution.subarraySum([1,2,3], 3)
print(answer)

# nums = [1,2,3], k = 3

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.