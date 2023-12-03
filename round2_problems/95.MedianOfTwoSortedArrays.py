from typing import List

# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 8:30
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        
solution = Solution()
answer = solution.findMedianSortedArrays([1,3],[2])
answer = solution.findMedianSortedArrays([1,3,5,7],[2,4,6,8])
print(answer)