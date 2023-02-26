from typing import List

# https://leetcode.com/problems/squares-of-a-sorted-array/editorial/
# Tags: Two Pointers
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        squaredList = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]**2
                left += 1
            else:
                square = nums[right]**2
                right -= 1

            squaredList[i] = square

        return squaredList


solution = Solution()
answer = solution.sortedSquares([-4,-1,0,3,10])
print(answer)