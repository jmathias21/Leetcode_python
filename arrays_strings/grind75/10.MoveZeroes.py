from typing import List

# https://leetcode.com/problems/move-zeroes/
# Tags: Two pointers, slow and fast pointers
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 11:00
    #
    # Uses a left (slow) and right (fast) pointer to do swaps of 0's and non 0's.
    # The slow and fast pointer move in unison to the right until they see a 0,
    # then the right pointer moves right until it sees a non-zero, and we swap
    # both numbers. Then the left pointer keeps moving right until it sees another
    # 0, and we keep repeating until all 0's are on the right side
    def moveZeroes(self, nums: List[int]) -> None:
        # set pointer to beginning of array
        slow = 0

        for fast in range(len(nums)):
            if nums[slow] == 0:
                if nums[fast] != 0:
                    nums[slow] = nums[fast]
                    nums[fast] = 0

            if nums[slow] != 0:
                slow += 1

        return nums
        
solution = Solution()
answer = solution.moveZeroes([1, 0])
answer = solution.moveZeroes([1])
answer = solution.moveZeroes([0, 1, 0, 3, 12])
print(answer)

# Example: [0, 1, 0, 3, 12]
#
# [0, 1, 0, 3, 12]
# S,F
# Start at zero
#
# [0, 1, 0, 3, 12]
#  S  F
# S sees zero so F checks current value for non-zero and moves
# forward by 1 since the current value is zero
#
# [1, 0, 0, 3, 12]
#  S  F
# F sees non-zero. Swap S and F values
#
# [1, 1, 0, 3, 12]
#     S  F
# Move S and F forward
#
# [1, 1, 0, 3, 12]
#        S  F
# Move S and F forward
#
# [1, 1, 3, 0, 12]
#        S  F
# S sees zero so F checks current value for non-zero. Since
# it is non-zero, we swap S and F values
#
# etc...