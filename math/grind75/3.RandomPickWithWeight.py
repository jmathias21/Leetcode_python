from typing import List
import bisect
import random

# https://leetcode.com/problems/random-pick-with-weight/
# Tags: Prefix sum, binary search
#
# Runtime Complexity: O(n)
# Space Complexity: O(n)
# Time: Not timed
#
# Calculate the prefix sums into an array. Each prefix sum will factor in each weight. So we can get a random
# number between 0 and the largest prefix sum, and then perform a binary search on the prefix sums to get the
# index it corresponds to
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.sum = 0
        for weight in w:
            self.sum += weight
            self.prefix_sum.append(self.sum)
        self.prefix_sum.pop()
        

    def pickIndex(self) -> int:
        rand = random.randint(0, self.sum - 1)
        return bisect.bisect_right(self.prefix_sum, rand)
        

obj = Solution([3,14,1,7])
param_1 = obj.pickIndex()
obj = Solution([4,2])
param_1 = obj.pickIndex()
obj = Solution([1,3,5,7])
param_1 = obj.pickIndex()