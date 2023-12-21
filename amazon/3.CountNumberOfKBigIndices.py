from typing import List
import heapq

# https://leetcode.com/problems/count-the-number-of-k-big-indices/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    def kBigIndices(self, nums: List[int], k: int) -> int:
        potential_indices1 = set()
        potential_indices2 = set()
        heap = []

        for i, num in enumerate(nums):
            if len(heap) == k and -num < heap[0]:
                potential_indices1.add(i)

            heapq.heappush(heap, -num)

            if len(heap) > k:
                heapq.heappop(heap)

        heap = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if len(heap) == k and -num < heap[0]:
                potential_indices2.add(i)

            heapq.heappush(heap, -num)

            if len(heap) > k:
                heapq.heappop(heap)

        return len(potential_indices1.intersection(potential_indices2))

        
solution = Solution()
answer = solution.kBigIndices([2,3,6,5,2,3], 2)
print(answer)