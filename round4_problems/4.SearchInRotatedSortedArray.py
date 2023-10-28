from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(log n)
    # Space Complexity: O()
    # Time: started 11:36, paused 11:55, started 12:21, finished 12:36
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def findPivot(left, right):
            mid = (left + right) // 2

            if nums[mid] < nums[mid - 1]:
                return mid
            elif nums[left] < nums[right]:
                return left
            else:
                if nums[mid] >= nums[left]:
                    return findPivot(mid + 1, right)
                else:
                    return findPivot(left, mid - 1)
                
        def search(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return search(mid + 1, right)
            else:
                return search(left, mid - 1)

            
        pivot = findPivot(0, len(nums) - 1)
        if target <= nums[-1]:
            return search(pivot, len(nums) - 1)
        else:
            return search(0, pivot - 1)

        
solution = Solution()
answer = solution.search([1,3,5], 5)
# answer = solution.search([1,2,3,4,5,6,7], 1) # 0
# answer = solution.search([5,1,2,3], 1) # 1
answer = solution.search([4,5,6,7,0,1,2], 3)
print(answer)