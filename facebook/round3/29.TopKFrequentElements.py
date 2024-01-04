from typing import List
from collections import Counter
import heapq

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n + klogn)
    # Space Complexity: O(n)
    # Time: started 9:09
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        heap = []

        for val, freq in frequencies.items():
            heap.append((-freq, val))
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        bucket = [[] for _ in range(max(frequencies.values()) + 1)]

        for val, freq in frequencies.items():
            bucket[freq].append(val)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                result.extend(bucket[i])
            if len(result) >= k:
                break

        return result
        
solution = Solution()
answer = solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
print(answer)