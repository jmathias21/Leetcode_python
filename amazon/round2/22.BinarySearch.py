from typing import List
import bisect


class Solution:

    def binary_search_iterative(self, nums: List[int], target: int, left_biased):
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
result = solution.binary_search_iterative([1, 3, 5, 7, 9, 10, 11, 12], 6, False)
result = solution.binary_search_iterative([1, 3, 5, 7, 9, 10, 11, 12, 14], 13, False)
result = solution.binary_search_iterative([1, 3, 5, 7, 9], 10, False)
result = solution.binary_search_iterative([1, 3, 5, 7, 9], 2, False)
result = solution.binary_search_iterative([1, 3, 5, 7, 9], 0, False)