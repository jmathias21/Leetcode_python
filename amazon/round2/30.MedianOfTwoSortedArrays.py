from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 7:05
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two pointers
        # build list from nums1 and nums2
        # track the middle point while building the list
        nums1 = deque(nums1)
        nums2 = deque(nums2)
        combined = []
        median_index = -1

        while nums1 or nums2:
            num1 = nums1[0] if nums1 else float('inf')
            num2 = nums2[0] if nums2 else float('inf')

            if num1 < num2:
                combined.append(nums1.popleft())
            else:
                combined.append(nums2.popleft())

            if len(combined) % 2 != 0:
                median_index += 1

        if len(combined) % 2 == 0:
            return (combined[median_index] + combined[median_index + 1]) / 2
        else:
            return combined[median_index]

        
solution = Solution()
answer = solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])
answer = solution.findMedianSortedArrays(nums1 = [1,2,4], nums2 = [2,2,5,7])
print(answer)