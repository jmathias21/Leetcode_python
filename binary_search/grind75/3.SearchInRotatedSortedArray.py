from typing import List

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Tags: binary search, rotated array
class Solution:

    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Use binary search to find the pivot point, then initiate a binary search
    # on the left or the right side of the pivot point depending on the target value
    # in order to find the target value's index
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rotate_index = self.findPivotIndex(nums, 0, n - 1, n)

        if target == nums[rotate_index]:
            return rotate_index
        elif target < nums[0]:
            return self.binarySearch(nums, target, rotate_index + 1, len(nums) - 1)
        else:
            return self.binarySearch(nums, target, 0, rotate_index)


    def findPivotIndex(self, nums, left, right, length):
        while left <= right:
            mid = (left + right) // 2

            if mid == length - 1 or nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return length - 1
    
    def binarySearch(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        return -1

    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Do a single binary search, but use some tricks to determine which side
    # of the array the target will be on
    def search2(self, nums: List[int], target: int) -> int:
        # set left and right pointers
        length = len(nums)
        left = 0
        right = length - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # we know that the middle value is on the left side of the pivot
            elif nums[mid] >= nums[left]:
                # if the target is on the left side of the pivot and smaller than
                # the middle value, we know its to the left of the middle value
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # we know the middle value is on the right side of the pivot
            else:
                # if the target is on the right side of the pivot and its greater than
                # the middle value, then we know its to the right of the middle value
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1



        
solution = Solution()
answer = solution.search([4,5,1,2,3], 1)
answer = solution.search([1], 0)
answer = solution.search([4,5,6,7,0,1,2], 0)
answer = solution.search([3,4,5,6,7,8,9,10,11,12,13,0,1], 0)
answer = solution.search([4,5,6,7,0,1,2], 0)
answer = solution.search([1,3,5], 1)
answer = solution.search([4,5,6,7,8,1,2,3], 2)
print(answer)