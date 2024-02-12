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
    
    def findValleyElement(self, nums: List[int]) -> int:

        def search(left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return search(mid + 1, right)
            else:
                return search(left, mid)
            
        return search(0, len(nums) - 1)

        
solution = Solution()
answer = solution.findValleyElement([1,2,0,1,0,3,0])
# answer = solution.findPeakElement([1,2,1,3,5,6,4])
print(answer)