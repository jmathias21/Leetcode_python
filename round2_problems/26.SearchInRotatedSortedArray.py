from typing import List
import bisect

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 38:00
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = len(nums) - 1

        def findPivotIndex(left, right):
            while left <= right:
                mid = (left + right) // 2

                if mid == length - 1 or nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            return length - 1

        pivot_index = findPivotIndex(left, right)
        if target < nums[pivot_index] and target < nums[0]:
            index = bisect.bisect_left(nums[pivot_index + 1:], target) + pivot_index + 1
            if index > length -1 or nums[index] != target:
                return -1
            return index
        else:
            index = bisect.bisect_left(nums[:pivot_index], target)
            if nums[index] != target:
                return -1
            return index

        
solution = Solution()
answer = solution.search([4,5,6,7,0,1,2], 3)
print(answer)

# [4,5,6,7,0,1,2]