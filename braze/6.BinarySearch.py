from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def searchRec(self, nums, target) -> int:
        def search(left, right):
            mid = (left + right) // 2
            
            if left > right:
                return -1
            
            if nums[mid] < target:
                return search(mid + 1, right)
            elif nums[mid] > target:
                return search(left, mid - 1)
            else:
                return mid
            
        return search(0, len(nums) - 1)
    
    def searchIterative(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
            
        return -1


        
solution = Solution()
answer = solution.functionName()
print(answer)