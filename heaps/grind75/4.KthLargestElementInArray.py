from typing import List
import heapq

# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Tags: Heap, Counting sort
class Solution:

    # Runtime Complexity: O(n log(k))
    # Space Complexity: O(n)
    # Time: 10:00
    def findKthLargestUsingHeap(self, nums: List[int], k: int) -> int:
        nums = [n * -1 for n in nums]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)
        return heapq.heappop(nums) * -1

    # Runtime Complexity: O(n * m)
    # Space Complexity: O()
    # Time: Not timed
    def findKthLargestUsingCountingSort(self, nums: List[int], k: int) -> int:
        smallest = min(nums)
        largest = max(nums)
        counts = [0] * ((largest - smallest) + 1)
        for i in range(len(nums)):
            counts[nums[i] - smallest] += 1

        for i in range(len(counts) - 1, -1, -1):
            k -= counts[i]
            if k <= 0:
                return i + smallest

        
solution = Solution()
answer = solution.findKthLargestUsingCountingSort([-5,-3,3,2,1,5,6,4], 2)
print(answer)