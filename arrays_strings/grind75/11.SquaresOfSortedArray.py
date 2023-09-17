from typing import List

# https://leetcode.com/problems/squares-of-a-sorted-array/editorial/
# Tags: Two Pointers
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 45:00
    #
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
            if abs(nums[left]) > nums[right]:
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

# Step 1: With initial list [-4, -1, 0, 3, 10], left points to -4 and right points to 10.
# Step 2: 10 squared is 100. So, the last position of squaredList becomes 100. Right pointer moves one step to the left.
# Step 3: Now, left is at -4 and right is at 3. 
# Step 4: -4 squared is 16. The second last position of squaredList becomes 16. Left pointer moves one step to the right.
# Step 5: Left is now at -1 and right is still at 3.
# Step 6: 3 squared is 9. The third last position of squaredList becomes 9. Right pointer moves one step to the left.
# Step 7: Left is still at -1 and right is now at 0.
# Step 8: -1 squared is 1. The fourth position from the last of squaredList becomes 1. Left pointer moves one step to the right.
# Step 9: Both left and right are now pointing at 0.
# Step 10: 0 squared is 0. The first position of squaredList becomes 0. 