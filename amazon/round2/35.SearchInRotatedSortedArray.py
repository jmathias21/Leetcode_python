from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def search(self, nums: List[int], target: int) -> int:
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

        def find_pivot(left, right):
            mid = (left + right) // 2

            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] <= nums[mid + 1]:
                if nums[mid] > nums[0]:
                    return find_pivot(mid, right)
                else:
                    return find_pivot(left, mid - 1)
                
        if nums[0] < nums[-1]:
            return search(0, len(nums) - 1)
                
        pivot = find_pivot(0, len(nums) - 1)
        print(pivot)
        if target >= nums[0]:
            return search(0, pivot)
        else:
            return search(pivot + 1, len(nums) - 1)

        
solution = Solution()
answer = solution.search(nums = [4,5,6,7,0,1,2], target = 0)
answer = solution.search(nums = [4,5,6,7,0,1,2], target = 5)
answer = solution.search(nums = [4,5,6,7,0,1,2], target = 2)
answer = solution.search(nums = [4,5,6,7,0,1,2], target = 4)
print(answer)