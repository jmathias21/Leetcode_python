from typing import List
import bisect
import random

# https://leetcode.com/problems/random-pick-with-weight
# Tags: Binary search
# Time: 16:00
class Solution:

    # Runtime Complexity: O(n)
    def __init__(self, w: List[int]):
        self.sum = 0
        self.d = []
        for weight in w:
            self.sum += weight
            self.d.extend([self.sum])
        

    # Runtime Complexity: O(logn)
    def pickIndex(self) -> int:
        rand = random.randint(0, self.sum - 1)
        val = bisect.bisect_right(self.d, rand)
        return val


obj = Solution([1,3,5])
param_1 = obj.pickIndex()
do = 0