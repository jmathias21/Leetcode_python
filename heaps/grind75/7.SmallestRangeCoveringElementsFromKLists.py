from typing import List
import heapq

# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Tags: 
class Solution:

    # Runtime Complexity: O(n * log(m))
    # Space Complexity: O(m)
    # Time: Not timed
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        largest = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            largest = max(largest, nums[i][0])

        smallest_range = [heap[0][0], largest]
        while True:
            _, i, j = heapq.heappop(heap)

            if j == len(nums[i]) - 1:
                break

            heapq.heappush(heap, (nums[i][j + 1], i, j + 1))
            largest = max(largest, nums[i][j + 1])

            if largest - heap[0][0] < smallest_range[1] - smallest_range[0]:
                smallest_range = [heap[0][0], largest]

        return smallest_range

        
solution = Solution()
answer = solution.smallestRange([[4,10,15,24,27],[0,9,12,27],[5,18,22,30]])
answer = solution.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
print(answer)