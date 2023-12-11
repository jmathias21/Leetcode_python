from typing import List

# https://leetcode.com/problems/move-zeroes/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:16
    def moveZeroes(self, nums: List[int]) -> None:
        fast = 0

        for i in range(len(nums)):
            fast = max(i, fast)
            if nums[i] == 0:
                while fast < len(nums) and nums[fast] == 0:
                    fast += 1
                if fast < len(nums):
                    nums[i], nums[fast] = nums[fast], nums[i]

        
solution = Solution()
answer = solution.moveZeroes([1, 0])
answer = solution.moveZeroes([0, 1, 0, 3, 12])
print(answer)

# [0, 1, 0, 3, 12]
