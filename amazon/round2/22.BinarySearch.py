from typing import List

class Solution:

    def binary_search_recursive(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        def search(nums, left, right):
            mid = (left + right) // 2

            if (left > right):
                return -1

            if nums[mid] < target:
                return search(nums, mid + 1, right)
            elif nums[mid] > target:
                return search(nums, left, mid - 1)
            else:
                return mid
            
        return search(nums, left, right)


    def binary_search_iterative(self, nums: List[int], target: int):
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
        
        print(str(left) + ' ' + str(right))
        return -1
    
solution = Solution()
result = solution.binary_search_recursive([1, 3, 5, 7, 9], 7)
result = solution.binary_search_iterative([1, 3, 5, 7, 9], 7)