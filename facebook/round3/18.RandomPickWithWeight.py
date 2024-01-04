from typing import List
import random
import bisect

# 
# Tags: 
# Runtime Complexity: O(logn)
# Space Complexity: O()
# Time: started 2:52
class Solution:


    def __init__(self, w: List[int]):
        self.weights = []
        s = 0
        for weight in w:
            s += weight
            self.weights.append(s)
        

    def pickIndex(self) -> int:
        rand = random.randint(0, self.weights[-1] - 1)
        index = bisect.bisect_right(self.weights, rand)
        return index


solution = Solution([1,3,4,5])
answer = solution.pickIndex()
print(answer)