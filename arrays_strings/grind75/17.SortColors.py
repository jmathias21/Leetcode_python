from typing import List

# https://leetcode.com/problems/sort-colors/
# Tags: Three pointers, Dutch National Flag Problem
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 45:00
    #
    # Uses three pointers. a left pointer that represents the right bound of 0's, a right pointer
    # that represents the left bound of 2's, and a current pointer that moves right and swaps its
    # own number with the left or the right pointers
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        curr = 0

        while curr <= right:
            # when the current number is 0, swap it with our left number
            if nums[curr] == 0:
                temp = nums[left]
                nums[left] = nums[curr]
                nums[curr] = temp
                left += 1
                curr += 1
            # when the current number is 1, leave it as is
            elif nums[curr] == 1:
                curr += 1
            # when the current number is 2, swap it with our right number
            else:
                temp = nums[right]
                nums[right] = nums[curr]
                nums[curr] = temp
                right -= 1

        
solution = Solution()
answer = solution.sortColors([2,0,2,1,1,0])
print(answer)

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

#  [2,0,2,1,1,0]
# L ^         ^ R
# C ^
# curr == 2, so swap it with right val. Move right pointer left

#  [0,0,2,1,1,2]
# L ^       ^ R
# C ^
# curr == 0, so swap it with left val. Move left and current pointers right

#  [0,0,2,1,1,2]
#   L ^     ^ R
#   C ^
# curr == 0, so swap it with left val. Move left and current pointers right

#  [0,0,2,1,1,2]
#     L ^   ^ R
#     C ^
# curr == 2, so swap it with right val. Move right pointer left

#  [0,0,1,1,2,2]
#     L ^ ^ R
#     C ^
# curr == 1, so move right

#  [0,0,1,1,2,2]
#     L ^ ^ R
#       C ^
# curr == 1, so move right

#  [0,0,1,1,2,2]
#     L ^ ^ R
#         C ^
# curr > right. The array is sorted