from typing import List
import heapq
from collections import deque

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(log(m + n))
    # Space Complexity: O(m + n)
    # Time: started 6:20
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        lo = []
        hi = []

        nums1 = deque(nums1)
        nums2 = deque(nums2)

        while nums1 or nums2:
            num = nums1.popleft() if nums1[0] <= nums2[0] else nums2.popleft()
            if num == float('inf'):
                break

            if len(lo) == len(hi):
                if hi:
                    heapq.heappush(lo, -heapq.heappop(hi))
                    heapq.heappush(hi, num)
                else:
                    heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)

        if len(lo) == len(hi):
            return (-lo[0] + hi[0]) / 2
        else:
            return -lo[0]

        
solution = Solution()
answer = solution.findMedianSortedArrays([1,3,5,6], [2,3,7])
print(answer)