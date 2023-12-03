from collections import Counter, defaultdict
from typing import List
import heapq

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n + k * logn)
    # Space Complexity: O(n)
    # Time: 12:00
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        heap = []

        for num, frequency in frequencies.items():
            heapq.heappush(heap, (-frequency, num))

        return [heapq.heappop(heap)[1] for _ in range(k)]

        
solution = Solution()
answer = solution.topKFrequent([1,1,1,2,2,3], 2)
print(answer)