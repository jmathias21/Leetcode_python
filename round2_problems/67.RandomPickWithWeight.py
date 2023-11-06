import bisect
from collections import defaultdict
import random
from typing import List

# 
# Tags: 
# Runtime Complexity: O()
# Space Complexity: O()
# Time: 21:00
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0] * len(w)
        sum = 0
        for i in range(len(w)):
            sum += w[i]
            self.prefix[i] = sum        

    def pickIndex(self) -> int:
        r = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, r)    


obj = Solution([1,3,5,8])

d = defaultdict(int)
for _ in range(10000):
    d[obj.pickIndex()] += 1