import bisect
from typing import List

# https://leetcode.com/problems/find-k-closest-elements/
# Tags: Binary search, sliding window
class Solution:

    # Runtime Complexity: O(log(N) + k)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Binary search to find the closest element to x. Initialize two pointers and then slide them
    # outward as we append elements to our array.
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k: return arr
        
        # Find the closest element and initialize two pointers
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1
        
        while right - left <= k:
            if left >= 0 and (right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]
    
    # Runtime Complexity: O(N)
    # Space Complexity: O(1)
    # Time: 25:00
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k: return arr

        left, right = 0, len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        return arr[left:right + 1]


solution = Solution()
answer = solution.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9)
answer = solution.findClosestElements([1,2,3,4,5], 4, 3)
answer = solution.findClosestElements([1,2,3,7,8], 3, 4)
answer = solution.findClosestElements([1,2,3,4,5], 4, -1)
print(answer)