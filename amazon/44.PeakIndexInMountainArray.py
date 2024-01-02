from typing import List

# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 7:53
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def search(left, right):
            mid = (left + right) // 2

            if left == right:
                return left

            if arr[mid] < arr[mid + 1]:
                return search(mid + 1, right)
            else:
                return search(left, mid)
            
        return search(0, len(arr) - 1)

        
solution = Solution()
answer = solution.peakIndexInMountainArray([0,2,4,8,10,15,7,5,2])
print(answer)