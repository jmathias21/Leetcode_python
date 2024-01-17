from collections import Counter, defaultdict, deque
import heapq
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O()
    # Time: started 4:39
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        bucket = [[] for _ in range(max(frequencies.values()) + 1)]

        for num, freq in frequencies.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                result.extend(bucket[i])
            if len(result) >= k:
                break

        return result

        
solution = Solution()
answer = solution.topKFrequent([1,1,1,2,2,3], 2)
print(answer)