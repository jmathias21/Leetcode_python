from typing import List

# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Tags: 
class Solution:

    # Runtime Complexity: O(log(n + m))
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Take smaller array and repeatedly binary search until we find a valid partition, where the partition of
    # both arrays only includes numbers that would be in the left side of a sorted, merged array
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        length = len(a) + len(b)
        half = length // 2

        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            a_left = a[i] if i >= 0 else float('-inf')
            a_right = a[i + 1] if (i + 1) < len(a) else float('inf')
            b_left = b[j] if j >= 0 else float('-inf')
            b_right = b[j + 1] if (j + 1) < len(b) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if length % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                else:
                    return min(a_right, b_right)
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1


solution = Solution()
answer = solution.findMedianSortedArrays([1,2], [3,4])
answer = solution.findMedianSortedArrays([1,3,4,5,8,9], [7,8,9,10])
print(answer)