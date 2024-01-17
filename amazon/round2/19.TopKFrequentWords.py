from collections import Counter
import heapq
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n log n)
    def topKFrequentUsingHeap(self, words: List[str], k: int) -> List[str]:
        frequencies = Counter(words)
        heap = []
        
        for num, freq in frequencies.items():
            heap.append((-freq, num))
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

    # Runtime Complexity: O(n log n)
    # Space Complexity: O()
    # Time: 
    def topKFrequentUsingBucket(self, words: List[str], k: int) -> List[str]:
        frequencies = Counter(words)
        bucket = [[] for _ in range(max(frequencies.values()) + 1)]

        for num, freq in frequencies.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            bucket[i].sort(reverse=True)
            while k > 0 and bucket[i]:
                result.append(bucket[i].pop())
                k -= 1
            if k <= 0:
                break

        return result

        
solution = Solution()
answer = solution.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4) # ["the","is","sunny","day"]
answer = solution.topKFrequent(["i","love","leetcode","i","love","coding"], 1)
print(answer)