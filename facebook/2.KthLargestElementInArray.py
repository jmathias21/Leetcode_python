from typing import List
import heapq

# 
# Tags: Counting Sort
class Solution:

    # Runtime Complexity: O(n logk)
    # Space Complexity: O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


    # Runtime Complexity: O(n + m)
    # Space Complexity: O(n)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        minimum = min(nums)
        counts = [0] * ((max(nums) - min(nums)) + 1)

        # O(n)
        for num in nums:
            counts[num - minimum ] += 1

        # O(m) where m is highest number
        sorted_nums = []
        for i, count in enumerate(counts):
            sorted_nums.extend([(i + minimum)] * count)

        return sorted_nums[-k]

        
solution = Solution()
answer = solution.findKthLargest([-5,-4,3,2,1,5,6,4], 2)
print(answer)