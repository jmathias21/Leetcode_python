from collections import Counter
from typing import List
import heapq

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 8:00
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        frequencies = [(-freq, word) for word, freq in counts.items()]
        heapq.heapify(frequencies)
        return [heapq.heappop(frequencies)[1] for _ in range(k)]

        
solution = Solution()
answer = solution.topKFrequent(["i","love","leetcode","i","love","coding"], 2)
print(answer)