from typing import List

# https://leetcode.com/problems/squares-of-a-sorted-array/editorial/
# Tags: Two Pointers
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Set a left pointer at the beginning of the array and a right
    # pointer at the end of the array. Then start at the end of the
    # array and loop through to the beginning. At each step, compare
    # the values at left and right pointers and add the squared absolute
    # value of the smaller number to a new list and move the
    # corresponding pointer forward
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
answer = solution.sortedSquares([-10,-5,-4,-2])
answer = solution.sortedSquares([-4,-1,0,3,10])
print(answer)

# Example: [-4,-1,0,3,10]
# [-4,-1,0,3,10]
#   ^         ^
# New arr: [0,0,0,0,100]
#
# [-4,-1,0,3,10]
#   ^      ^
# New arr: [0,0,0,16,100]
#
# [-4,-1,0,3,10]
#   ^    ^
# New arr: [0,0,9,16,100]
# etc...