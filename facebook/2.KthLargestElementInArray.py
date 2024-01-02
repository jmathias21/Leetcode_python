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
            heapq.heappush(num)
            if len(heap) > k:
                heapq.heappop(num)

        return heap[0]


    # Runtime Complexity: O(n + m)
    # Space Complexity: O(n)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        minimum = min(nums)
        maximum = max(nums)
        counts = [0] * (abs(minimum) + maximum + 1)
        for num in nums:
            counts[num + abs(minimum)] += 1

        i = abs(minimum) + maximum
        while k > 0:
            k -= counts[i]
            i -= 1
        return (i + 1) - abs(minimum)


        
solution = Solution()
answer = solution.findKthLargest2([-5,-4,3,2,1,5,6,4], 2)
print(answer)