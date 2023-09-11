from typing import List

# https://leetcode.com/problems/binary-search/
# Tags: Binary Search, Two Pointers
class Solution:
    
    # Runtime Complexity: O(log n)
    # Space Complexity: O(log n)
    def searchRecursive(self, nums: List[int], target: int) -> int:
        return self.rec(nums, target, 0, len(nums) - 1)

    def rec(self, nums: List[int], target: int, left: int, right: int) -> int:
        mid = int((right + left) / 2)

        # base case
        if (nums[mid] == target):
            return mid
        
        if (left > right):
            return -1
        
        # recursive case    
        if (nums[mid] < target):
            return self.rec(nums, target, mid + 1, right)
        else:
            return self.rec(nums, target, left, mid - 1)
        
        

    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    def searchIterative(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1

        while (left <= right):
            mid = int((right + left) / 2)
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                return mid
            
        return -1


solution = Solution()
answer = solution.searchRecursive([-1,0,3,5,9,12], 13)
print(answer)

solution = Solution()
answer = solution.searchIterative([-1,0,3,5,9,12], 9)
print(answer)