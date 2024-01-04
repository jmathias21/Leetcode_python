from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(logn)
    # Space Complexity: O(logn)
    # Time: started 11:21
    def findPeakElement(self, nums: List[int]) -> int:

        def search(left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2

            if nums[mid] >= nums[mid + 1]:
                return search(left, mid)
            else:
                return search(mid + 1, right)
            
        return search(0, len(nums) - 1)

        
solution = Solution()
answer = solution.findPeakElement([1,2,1,3,5,6,4])
print(answer)