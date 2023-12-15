from typing import List
import heapq

# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Tags: 
class Solution:

    # Runtime Complexity: O(n logk)
    # Space Complexity: O(k)
    # Time: started 8:18
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

        
solution = Solution()
answer = solution.findKthLargest([3,2,1,5,6,4], 2)
print(answer)