from typing import List
from collections import Counter

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 30:00
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
answer = solution.topKFrequent([-1,-1], 1)
answer = solution.topKFrequent([1,1,1,2,2,3], 2)
print(answer)