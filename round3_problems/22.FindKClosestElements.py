from typing import List
import bisect

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(klogk)
    # Space Complexity: O()
    # Time: started 3:37
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1

        while right - left <= k:
            if left >= 0 and (right == len(arr) or arr[right] - x >= x - arr[left]):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]



        
solution = Solution()
answer = solution.findClosestElements([-2,-1,1,2,3,4,5], 7, 3)
print(answer)