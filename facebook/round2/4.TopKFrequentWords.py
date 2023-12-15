from typing import List
from collections import Counter
import heapq

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:02
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # create hash map of words as keys and store their associated count as the value
        cnt = Counter(words)

        # create a max heap of tuples, where the first element is the frequency and the second
        # element is the word
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapq.heapify(heap)

        # O(k log n) because popping is log n and we do it k times
        return [heapq.heappop(heap)[1] for _ in range(k)]
        

        
solution = Solution()
answer = solution.topKFrequent(["i","love","leetcode","i","love","coding"], 2)
print(answer)