from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:50
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(left, right):
            mid = (left + right) // 2

            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                return mid
            elif nums[left] < nums[mid]:
                return findPivot(mid + 1, right)
            else:
                return findPivot(left, mid - 1)


        def search(left, right):
            mid = (left + right) // 2

        return findPivot(0, len(nums) - 1)
            

        
solution = Solution()
# answer = solution.search([3,1], 1)
# answer = solution.search([1], 0)
#answer = solution.search([7,1,2,3,5,6], 1)
answer = solution.search([4,5,6,7,0,1,2], 3)
print(answer)