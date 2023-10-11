from typing import List

# https://leetcode.com/problems/container-with-most-water/
# Tags: Two pointers
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 6:00
    #
    # Use a left and a right pointer. Calculate the max water between numbers at left and right
    # pointers, then move the shorter pointer forward. Return the max water.
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            max_water = max(max_water, min(height[right], height[left]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
        
solution = Solution()
answer = solution.maxArea([1,8,6,2,5,4,8,3,7])
print(answer)