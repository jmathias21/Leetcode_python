from collections import Counter, defaultdict
from heapq import heapify, heappop
from typing import List

from sortedcontainers import SortedDict

# https://leetcode.com/problems/top-k-frequent-words
# Tags: Max Heap
class Solution:

    # Runtime Complexity: O(n + k log n)
    # Space Complexity: O(n)
    # Time: Not timed
    def topKFrequentUsingMaxHeap(self, words: List[str], k: int) -> List[str]:
        # create hash map of words as keys and store their associated count as the value
        cnt = Counter(words)

        # create a max heap of tuples, where the first element is the frequency and the second
        # element is the word
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapify(heap)

        # O(k log n) because popping is log n and we do it k times
        return [heappop(heap)[1] for _ in range(k)]

        
solution = Solution()
answer = solution.topKFrequent(["a","aa","aaa"], 2)
answer = solution.topKFrequent(["love","leetcode","i","i","love","coding"], 1)
answer = solution.topKFrequent(["love","leetcode","i","i","love","coding"], 2)
print(answer)