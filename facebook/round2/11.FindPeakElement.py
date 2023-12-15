from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(logn)
    # Space Complexity: O(logn)
    # Time: 11:00
    def findPeakElement(self, nums: List[int]) -> int:
        def search(left, right):
            if left == right:
                return left

            mid = (left + right) // 2

            # going uphill
            if nums[mid] < nums[mid + 1]:
                return search(mid + 1, right)
            else:
                return search(left, mid)
            
        return search(0, len(nums) - 1)


        
solution = Solution()
answer = solution.findPeakElement([1,2,3,1])
print(answer)