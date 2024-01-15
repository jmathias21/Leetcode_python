from typing import List
import bisect

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1

        while k > 0:
            if left >= 0 and (right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1
            k -= 1

        return arr[left + 1:right]

        
solution = Solution()
answer = solution.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9)
print(answer)