from typing import List
import bisect

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(logn + k)
    # Space Complexity: O()
    # Time: started 4:16
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1
        
        while right - left <= k:
            if left < 0:
                right = left + k + 1
                break

            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]



        
solution = Solution()
answer = solution.findClosestElements([3,4,5,6], 3, 3)
answer = solution.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9)
print(answer)