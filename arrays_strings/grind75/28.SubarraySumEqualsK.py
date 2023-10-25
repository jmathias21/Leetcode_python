from collections import defaultdict
from typing import List

# https://leetcode.com/problems/subarray-sum-equals-k/
# Tags: Prefix sum, hash map
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Use prefix sum to store sum counts in a hash map. If our current sum minus our target k equals
    # a key in the hash map, it means that we can essentially subtract that part of the array to arrive
    # at our answer
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        total = 0

        s = 0

        for i in range(len(nums)):
            s += nums[i]
            diff = s - k

            if diff in prefix:
                total += prefix[diff]

            prefix[s] += 1

        return total

        
solution = Solution()
answer = solution.subarraySum([1,1,1], 2)
answer = solution.subarraySum([-1,-1,1], 0)
answer = solution.subarraySum([1,2,3], 3)
answer = solution.subarraySum([1], 0)
answer = solution.subarraySum([1,1,1], 2)
answer = solution.subarraySum([1,1,3,3,4,5], 4)
print(answer)