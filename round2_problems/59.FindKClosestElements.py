import bisect
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 35:00
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k: return arr

        left = bisect.bisect_left(arr, x) - 1
        right = left + 1

        while k > 0:
            if left == -1 or (right <= len(arr) - 1 and abs(x - arr[left]) > abs(arr[right] - x)):
                right += 1
            else:
                left -= 1

            k -= 1

        return arr[left + 1:right]


        
solution = Solution()
answer = solution.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9)
answer = solution.findClosestElements([1,2,3,4,5], 4, 3)
answer = solution.findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5)
answer = solution.findClosestElements([1,2,3,4,5], 4, -1)
answer = solution.findClosestElements([1,2,3,4,5,6,7,8], 2, 5)
print(answer)