from typing import List

# https://leetcode.com/problems/binary-search/
# Tags: Binary Search
class Solution:
    
    # Runtime Complexity: O(log n)
    # Space Complexity: O(log n)
    def searchRecursive(self, nums: List[int], target: int) -> int:
        return self.rec(nums, target, 0, len(nums) - 1)

    def rec(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        middle = int((left + right) / 2)

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return self.rec(nums, target, left, middle - 1)
        else:
            return self.rec(nums, target, middle + 1, right)

    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    def searchIterative(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while True:
            if left > right:
                return -1

            middle = int((left + right) / 2)

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1


solution = Solution()
answer = solution.searchRecursive([-1,0,3,5,9,12], 9)
print(answer)

answer = solution.searchIterative([-1,0,3,5,9,12], 9)
print(answer)