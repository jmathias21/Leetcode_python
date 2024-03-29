from collections import Counter
from typing import List

# https://leetcode.com/problems/top-k-frequent-elements/
# Tags: Hash Map, Bucket Sort
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 12:00
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        frequencies = [[] for _ in range(max(counts.values()) + 1)]

        for num, frequency in counts.items():
            frequencies[frequency].append(num)

        output = []
        for i in range(len(frequencies) - 1, -1, -1):
            if frequencies[i]:
                output.extend(frequencies[i])
            if len(output) >= k:
                break

        return output

        
solution = Solution()
answer = solution.topKFrequent([1,1,1,2,2,3], 2)
print(answer)